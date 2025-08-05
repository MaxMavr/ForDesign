from typing import Union, Tuple
from PIL import Image
import re
from random import randint
from programs.prints.color_output import true_false_out

HEX = str
RGB = Tuple[int, int, int]
NRGB = Tuple[float, float, float]
CMYK = Tuple[int, int, int, int]

HSV = Tuple[int, float, float]
HSL = Tuple[int, float, float]

YUV = Tuple[float, float, float]
XYZ = Tuple[float, float, float]
LAB = Tuple[float, float, float]

COLOR = Tuple[HEX, RGB, CMYK]
INPUT_COLOR = Union[HEX, RGB, CMYK]

Kr = 0.2627
Kb = 0.0593


# TODO: Исправить или проверить XYZ


def show_color(color: INPUT_COLOR):
    color = decoding_color(color)
    color_img = Image.new('RGB', (300, 300), color[0])
    color_img.show(title=f'HEX {color[0]}\nRGB {color[1]}\nCMYK {color[2]}')
    del color_img


def format_hex(color: HEX) -> HEX:
    matches = re.findall(r'#?([\da-fA-F]{6})', color)

    if len(matches) != 1:
        return '#000000'

    return f'#{matches[0].upper()}'


def format_rgb(color: RGB) -> RGB:
    format_color = (
        max(0, min(255, color[0])),
        max(0, min(255, color[1])),
        max(0, min(255, color[2])),
    )
    return format_color


def format_cmyk(color: CMYK) -> CMYK:
    format_color = (
        max(0, min(100, color[0])),
        max(0, min(100, color[1])),
        max(0, min(100, color[2])),
        max(0, min(100, color[3]))
    )
    return format_color


def format_hsl(color: HSL) -> HSL:
    format_color = (
        max(0, min(360, color[0])),
        max(0.0, min(100.0, color[1])),
        max(0.0, min(100.0, color[2])),
    )
    return format_color


def format_yuv(color: YUV) -> YUV:
    format_color = (
        max(-0.5, min(0.5, color[0])),
        max(-0.5, min(0.5, color[1])),
        max(-0.5, min(0.5, color[2])),
    )
    return format_color


def format_hsv(color: HSV) -> HSV:
    return format_hsl(color)


def normalize_rgb(color: RGB) -> NRGB:
    r, g, b = format_rgb(color)
    return r / 255, g / 255, b / 255


def rgb2hex(color: RGB) -> HEX:
    r, g, b = format_rgb(color)

    hex_r = hex(r).upper()[2:].zfill(2)
    hex_g = hex(g).upper()[2:].zfill(2)
    hex_b = hex(b).upper()[2:].zfill(2)

    return f'#{hex_r}{hex_g}{hex_b}'


def rgb2cmyk(color: RGB) -> CMYK:
    r, g, b = normalize_rgb(color)

    k = 1 - max(r, g, b)

    if k == 1:
        c = 0
        m = 0
        y = 0
    else:
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)

    return round(c * 100), round(m * 100), round(y * 100), round(k * 100)


def rgb2hsl(color: RGB) -> HSL:
    """Hue Saturation Lightness"""
    r, g, b = normalize_rgb(color)

    ch_max = max(r, g, b)
    ch_min = min(r, g, b)
    delta = ch_max - ch_min

    if delta == 0:
        h = 0
    elif ch_max == r:
        h = (60 * ((g - b) / delta) + 360) % 360
    elif ch_max == g:
        h = (60 * ((b - r) / delta) + 120) % 360
    elif ch_max == b:
        h = (60 * ((r - g) / delta) + 240) % 360
    else:
        h = 360

    l = (ch_max + ch_min) / 2

    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))

    return round(h), s * 100, l * 100


def rgb2hsv(color: RGB) -> HSV:
    """Hue Saturation Value (Brightness)"""
    r, g, b = normalize_rgb(color)

    ch_max = max(r, g, b)
    ch_min = min(r, g, b)
    delta = ch_max - ch_min

    if delta == 0:
        h = 0
    elif ch_max == r:
        h = (60 * ((g - b) / delta) + 360) % 360
    elif ch_max == g:
        h = (60 * ((b - r) / delta) + 120) % 360
    elif ch_max == b:
        h = (60 * ((r - g) / delta) + 240) % 360
    else:
        h = 360

    if ch_max == 0:
        s = 0
    else:
        s = delta / ch_max

    v = ch_max

    return round(h), s * 100, v * 100


def rgb2yuv(color: RGB) -> YUV:
    r, g, b = normalize_rgb(color)

    y = Kr * r + (1 - Kr - Kb) * g + Kb * b
    u = b - y
    v = r - y

    return y, u, v


def hex2rgb(color: HEX) -> RGB:
    matches = re.findall(r'#?([\da-fA-F]{6})', format_hex(color))

    r = matches[0][0:2]
    g = matches[0][2:4]
    b = matches[0][4:6]

    return int(r, 16), int(g, 16), int(b, 16)


def cmyk2rgb(color: CMYK) -> RGB:
    c, k, m, y = format_cmyk(color)
    c, k, m, y = c / 100, k / 100, m / 100, y / 100

    print(c, k, m, y)

    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)

    return round(r), round(g), round(b)


def hsv2rgb(color: HSV) -> RGB:
    h, s, v = format_hsv(color)
    h, s, v = h / 60, s / 100, v / 100

    c = v * s

    x = c * (1 - abs(h % 2 - 1))

    m = v - c

    if 0 <= h < 1:
        r, g, b = c, x, 0
    elif 1 <= h < 2:
        r, g, b = x, c, 0
    elif 2 <= h < 3:
        r, g, b = 0, c, x
    elif 3 <= h < 4:
        r, g, b = 0, x, c
    elif 4 <= h < 5:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    return round((r + m) * 255), round((g + m) * 255), round((b + m) * 255)


def hsl2rgb(color: HSL) -> RGB:
    h, s, l = format_hsl(color)
    h, s, l = h / 60, s / 100, l / 100

    c = (1 - abs(2 * l - 1)) * s

    x = c * (1 - abs(h % 2 - 1))

    m = l - c / 2

    if 0 <= h < 1:
        r, g, b = c, x, 0
    elif 1 <= h < 2:
        r, g, b = x, c, 0
    elif 2 <= h < 3:
        r, g, b = 0, c, x
    elif 3 <= h < 4:
        r, g, b = 0, x, c
    elif 4 <= h < 5:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    return round((r + m) * 255), round((g + m) * 255), round((b + m) * 255)


def yuv2rgb(color: YUV) -> RGB:
    y, u, v = format_yuv(color)

    r = y + v
    g = y - ((Kr * v + Kb * u) / (1 - Kr - Kb))
    b = y + u

    return round(r * 255), round(g * 255), round(b * 255)


def hex2cmyk(color: HEX) -> CMYK:
    rgb = hex2rgb(color)
    return rgb2cmyk(rgb)


def cmyk2hex(color: CMYK) -> HEX:
    rgb = cmyk2rgb(color)
    return rgb2hex(rgb)


def decoding_hex(color: HEX) -> COLOR:
    """
    :param color: Цвет в формате HEX.
    :return: Список цвета в форматах HEX, RGB и CMYK.
    """

    hex_color = format_hex(color)
    rgb_color = hex2rgb(color)
    cmyk_color = hex2cmyk(color)

    return hex_color, rgb_color, cmyk_color


def decoding_rgb(color: RGB) -> COLOR:
    """
    :param color: Цвет в формате RGB.
    :return: Список цвета в форматах HEX, RGB и CMYK.
    """

    hex_color = rgb2hex(color)
    rgb_color = format_rgb(color)
    cmyk_color = rgb2cmyk(color)

    return hex_color, rgb_color, cmyk_color


def decoding_cmyk(color: CMYK) -> COLOR:
    """
    :param color: Цвет в формате CMYK.
    :return: Список цвета в форматах HEX, RGB и CMYK.
    """

    hex_color = cmyk2hex(color)
    rgb_color = cmyk2rgb(color)
    cmyk_color = format_cmyk(color)

    return hex_color, rgb_color, cmyk_color


def decoding_color(color: INPUT_COLOR):
    """
    :param color: Цвет в формате HEX, RGB или CMYK.
    :return: Список цвета в форматах HEX, RGB и CMYK.
    """

    if isinstance(color, str):
        return decoding_hex(color)
    else:
        if len(color) == 3:
            return decoding_rgb(color)
        if len(color) == 4:
            return decoding_cmyk(color)


def calc_brightness(color: INPUT_COLOR):
    """
    :param color: Цвет в формате HEX, RGB или CMYK.
    :return: Яркость в диапазоне [0, 255]
    """
    r, g, b = decoding_color(color)[1]
    return 0.299 * r + 0.587 * g + 0.114 * b


if __name__ == "__main__":

    def check_lists(color1, color2):
        for i in range(len(color1)):
            if abs(color1[i] - color2[i]) > 1:
                return False
        return True

    rgb_colors = []

    def check_color(color1, infunc, outfunc):
        print(color1)

        incolor = infunc(color1)
        print(incolor)
        outcolor = outfunc(incolor)

        print(true_false_out(
            str(outcolor),
            check_lists(
                color1,
                outcolor)))

        return check_lists(
                color1,
                outcolor)


    for _ in range(100):
        rgb_colors.append(
            (randint(0, 255),
             randint(0, 255),
             randint(0, 255)))

    hex_quantity = 0
    cmyk_quantity = 0
    hsl_quantity = 0
    hsv_quantity = 0
    yuv_quantity = 0

    # print('\n\nHEX - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    # for icolor in rgb_colors:
    #     if check_color(icolor, rgb2hex, hex2rgb):
    #         hex_quantity += 1

    print('\n\nCMYK - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    for icolor in rgb_colors:
        if check_color(icolor, rgb2cmyk, cmyk2rgb):
            cmyk_quantity += 1

    # print('\n\nHSL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    # for icolor in rgb_colors:
    #     if check_color(icolor, rgb2hsl, hsl2rgb):
    #         hsl_quantity += 1
    #
    # print('\n\nHSV - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    # for icolor in rgb_colors:
    #     if check_color(icolor, rgb2hsv, hsv2rgb):
    #         hsv_quantity += 1

    print('\n\nYUV - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    for icolor in rgb_colors:
        if check_color(icolor, rgb2yuv, yuv2rgb):
            yuv_quantity += 1

    len_ = len(str(len(rgb_colors)))
    print('\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print(f'     {len(rgb_colors)}')
    # print(f'HEX  {str(hex_quantity).ljust(100)}')
    print(f'CMYK {str(cmyk_quantity).ljust(100)}')
    # print(f'HSL  {str(hsl_quantity).ljust(100)}')
    # print(f'HSV  {str(hsv_quantity).ljust(100)}')
    print(f'YUV  {str(yuv_quantity).title()}')

