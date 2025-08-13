from math import sqrt
from utils.color import Color


def distance(color1: Color, color2: Color) -> float:
    return sqrt(sum((v1 - v2)**2 for v1, v2 in zip(color1.rgba, color2.rgba)))


def blend(color1: Color, color2: Color) -> Color:
    def blend_channel(value1: float, value2: float, alpha1: float, alpha2: float, out_alpha: float) -> float:
        return (value1 * alpha1 + value2 * alpha2 * (1 - alpha1)) / out_alpha

    a1, a2 = color1.a / 255, color2.a / 255
    out_a = a1 + a2 * (1 - a1)

    if not out_a:
        return Color(0, 0, 0, 0)

    r = blend_channel(color1.r, color2.r, a1, a2, out_a)
    g = blend_channel(color1.g, color2.g, a1, a2, out_a)
    b = blend_channel(color1.b, color2.b, a1, a2, out_a)

    return Color(r, g, b, out_a * 255)
