from math import sqrt
from typing import Tuple
from utils.color import Color
from PIL import Image


def show_color(self, size: Tuple[int, int] = (300, 300)):
    img = Image.new('RGB', size, self.rgb)
    img.show(
        title=f'Color(HEX: {self.hexa}, RGB: {self.rgba}, CMYK: {self.cmyk}, CSS_name: {self.css_name}, HSV: {self.hsv}, HSL: {self.hsl})')
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


def red_channel(color: Color) -> Color:
    """Выделить красный канал"""
    red_color = color - (0, 255, 255)
    red_color.a = 255
    return red_color


def green_channel(color: Color) -> Color:
    """Выделить зелёный канал"""
    green_color = color - (255, 0, 255)
    green_color.a = 255
    return green_color


def blue_channel(color: Color) -> Color:
    """Выделить синий канал"""
    blue_color = color - (255, 255, 0)
    blue_color.a = 255
    return blue_color


def alpha_channel(color: Color) -> Color:
    """Выделить альфа-канал как оттенок серого"""
    gray_value = color.a
    return Color(gray_value, gray_value, gray_value, 255)


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
