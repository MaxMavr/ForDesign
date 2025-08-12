from math import sqrt
from typing import Tuple
from utils.color import Color
from PIL import Image


def show_color(self, size: Tuple[int, int] = (300, 300)):
    img = Image.new('RGB', size, self.rgb)
    img.show(title=f'Color(HEX: {self.hexa}, RGB: {self.rgba}, CMYK: {self.cmyk}, CSS_name: {self.css_name}, HSV: {self.hsv}, HSL: {self.hsl})')
    del img


def grayscale(color: Color) -> Color:
    """Преобразовать цвет в оттенок серого по яркости."""
    _, _, _, a = color.rgba
    g = int(color.brightness)
    return Color(g, g, g, a)


def invert(color: Color) -> Color:
    """Обратный цвет"""
    return -color


def complement(color: Color) -> Color:
    """Возвращает дополнительный цвет (напротив в цветовом круге)"""
    h, s, l = color.hsl
    h = (h + 180) % 360
    return Color.from_hsl((h, s, l))


def triad(color: Color) -> Tuple[Color, Color]:
    """Возвращает два дополнительных цвета для триадной схемы"""
    h, s, l = color.hsl
    color1 = Color.from_hsl(((h + 120) % 360, s, l))
    color2 = Color.from_hsl(((h + 240) % 360, s, l))
    return color1, color2


def analogous(color: Color, shift: int = 30) -> Tuple[Color, Color]:
    """Аналогичные цвета ±shift градусов по hue"""
    h, s, l = color.hsl
    color1 = Color.from_hsl(((h - shift) % 360, s, l))
    color2 = Color.from_hsl(((h + shift) % 360, s, l))
    return color1, color2


def distance(color1: Color, color2: Color) -> float:
    return sqrt(sum((v1 - v2)**2 for v1, v2 in zip(color1.rgba, color2.rgba)))


def blend(color1: Color, color2: Color) -> Color:
    def _blend_channel(value1, alpha1, value2, alpha2):
        if alpha1 == 0 and alpha2 == 0:
            return 0
        return int(
            (value1 * alpha1 + value2 * alpha2 * (255 - alpha1) / 255) /
            (alpha1 + alpha2 * (255 - alpha1) / 255))

    def _blend_alpha(alpha1, alpha2):
        return int(alpha1 + alpha2 * (255 - alpha1) / 255)

    r1, g1, b1, a1 = color1.rgba
    r2, g2, b2, a2 = color2.rgba

    out_a = _blend_alpha(a1, a2)
    r = _blend_channel(r1, a1, r2, a2)
    g = _blend_channel(g1, a1, g2, a2)
    b = _blend_channel(b1, a1, b2, a2)
    return Color(r, g, b, out_a)
