import os
import random
from typing import List, Tuple, Union, Callable
import numpy as np
from programs.svg.item import SVGrect, SVGline
from programs import svg

BAYER_8x8 = np.array([
    [0, 48, 12, 60, 3, 51, 15, 63],
    [32, 16, 44, 28, 35, 19, 47, 31],
    [8, 56, 4, 52, 11, 59, 7, 55],
    [40, 24, 36, 20, 43, 27, 39, 23],
    [2, 50, 14, 62, 1, 49, 13, 61],
    [34, 18, 46, 30, 33, 17, 45, 29],
    [10, 58, 6, 54, 9, 57, 5, 53],
    [42, 26, 38, 22, 41, 25, 37, 21],
]) / 64.0


def get_gradient_value(x, y, x0, y0, x1, y1):
    dx, dy = x1 - x0, y1 - y0
    if dx == dy == 0:
        return 0
    t = ((x - x0) * dx + (y - y0) * dy) / (dx * dx + dy * dy)
    return max(0, min(1, t))


def pattern_dither(x: int, y: int, brightness: Union[int, float]) -> bool:
    threshold = BAYER_8x8[y % 8][x % 8]
    return brightness > threshold


def noise_dither(x: int, y: int, brightness: Union[int, float]) -> bool:
    threshold = random.random()
    return brightness > threshold


def make_dither(width: int,
                height: int,
                line: SVGline,
                dither_algorithm: Callable[[int, int, float], bool]) -> list[tuple[int, int]]:
    points = []
    for y in range(height):
        for x in range(width):
            brightness = get_gradient_value(x, y, line.x1, line.y1, line.x2, line.y2)
            if dither_algorithm(x, y, brightness):
                points.append((x, y))
    return points


def make_mixed_dither(
    width: int,
    height: int,
    brightness_line: SVGline,
    mix_line: SVGline,
    dither_a: Callable[[int, int, float], bool],
    dither_b: Callable[[int, int, float], bool]
) -> list[tuple[int, int]]:
    points = []
    for y in range(height):
        for x in range(width):
            brightness = get_gradient_value(x, y, brightness_line.x1, brightness_line.y1, brightness_line.x2, brightness_line.y2)
            mix_ratio = get_gradient_value(x, y, mix_line.x1, mix_line.y1, mix_line.x2, mix_line.y2)
            if random.random() < mix_ratio:
                if dither_b(x, y, brightness):
                    points.append((x, y))
            else:
                if dither_a(x, y, brightness):
                    points.append((x, y))
    return points


if __name__ == '__main__':
    output_width, output_height = 297, 420
    brightness_line = SVGline(110, 130, 190, 380, stroke="green", stroke_width=1)
    mix_line = SVGline(151, 258, 236, 231, stroke="red", stroke_width=1)

    def save_svg(points: List[Tuple[int, int]], filename):
        rects: List[str] = [brightness_line.svg, mix_line.svg]
        rects.extend(SVGrect(x, y, 1, 1).svg for x, y in points)

        svg.file.make(
            width=output_width,
            height=output_height,
            styles=None,
            content=rects,
            output_path=os.path.join(os.path.dirname(__file__), "output", filename),
            attributes={"shape-rendering": "crispEdges"}
        )

    points = make_dither(output_width, output_height, brightness_line, pattern_dither)
    save_svg(points, "Dither-PATTERN.svg")

    points = make_dither(output_width, output_height, brightness_line, noise_dither)
    save_svg(points, "Dither-NOISE.svg")

    points = make_mixed_dither(output_width, output_height, brightness_line, mix_line, noise_dither, pattern_dither)
    save_svg(points, "Dither-NOISE-to-PATTERN.svg")

    points = make_mixed_dither(output_width, output_height, brightness_line, mix_line, pattern_dither, noise_dither)
    save_svg(points, "Dither-PATTERN-to-NOISE.svg")
