from math import sqrt
from random import randint
from typing import Tuple, Dict, Union, Optional
import re


css_named_colors: Dict[str, Tuple[int, int, int, int]] = {
    'aliceblue': (240, 248, 255, 255),
    'antiquewhite': (250, 235, 215, 255),
    'aqua': (0, 255, 255, 255),
    'aquamarine': (127, 255, 212, 255),
    'azure': (240, 255, 255, 255),
    'beige': (245, 245, 220, 255),
    'bisque': (255, 228, 196, 255),
    'black': (0, 0, 0, 255),
    'blanchedalmond': (255, 235, 205, 255),
    'blue': (0, 0, 255, 255),
    'blueviolet': (138, 43, 226, 255),
    'brown': (165, 42, 42, 255),
    'burlywood': (222, 184, 135, 255),
    'cadetblue': (95, 158, 160, 255),
    'chartreuse': (127, 255, 0, 255),
    'chocolate': (210, 105, 30, 255),
    'coral': (255, 127, 80, 255),
    'cornflowerblue': (100, 149, 237, 255),
    'cornsilk': (255, 248, 220, 255),
    'crimson': (220, 20, 60, 255),
    'cyan': (0, 255, 255, 255),
    'darkblue': (0, 0, 139, 255),
    'darkcyan': (0, 139, 139, 255),
    'darkgoldenrod': (184, 134, 11, 255),
    'darkgray': (169, 169, 169, 255),
    'darkgreen': (0, 100, 0, 255),
    'darkgrey': (169, 169, 169, 255),
    'darkkhaki': (189, 183, 107, 255),
    'darkmagenta': (139, 0, 139, 255),
    'darkolivegreen': (85, 107, 47, 255),
    'darkorange': (255, 140, 0, 255),
    'darkorchid': (153, 50, 204, 255),
    'darkred': (139, 0, 0, 255),
    'darksalmon': (233, 150, 122, 255),
    'darkseagreen': (143, 188, 143, 255),
    'darkslateblue': (72, 61, 139, 255),
    'darkslategray': (47, 79, 79, 255),
    'darkslategrey': (47, 79, 79, 255),
    'darkturquoise': (0, 206, 209, 255),
    'darkviolet': (148, 0, 211, 255),
    'deeppink': (255, 20, 147, 255),
    'deepskyblue': (0, 191, 255, 255),
    'dimgray': (105, 105, 105, 255),
    'dimgrey': (105, 105, 105, 255),
    'dodgerblue': (30, 144, 255, 255),
    'firebrick': (178, 34, 34, 255),
    'floralwhite': (255, 250, 240, 255),
    'forestgreen': (34, 139, 34, 255),
    'fuchsia': (255, 0, 255, 255),
    'gainsboro': (220, 220, 220, 255),
    'ghostwhite': (248, 248, 255, 255),
    'gold': (255, 215, 0, 255),
    'goldenrod': (218, 165, 32, 255),
    'gray': (128, 128, 128, 255),
    'green': (0, 128, 0, 255),
    'greenyellow': (173, 255, 47, 255),
    'grey': (128, 128, 128, 255),
    'honeydew': (240, 255, 240, 255),
    'hotpink': (255, 105, 180, 255),
    'indianred': (205, 92, 92, 255),
    'indigo': (75, 0, 130, 255),
    'ivory': (255, 255, 240, 255),
    'khaki': (240, 230, 140, 255),
    'lavender': (230, 230, 250, 255),
    'lavenderblush': (255, 240, 245, 255),
    'lawngreen': (124, 252, 0, 255),
    'lemonchiffon': (255, 250, 205, 255),
    'lightblue': (173, 216, 230, 255),
    'lightcoral': (240, 128, 128, 255),
    'lightcyan': (224, 255, 255, 255),
    'lightgoldenrodyellow': (250, 250, 210, 255),
    'lightgray': (211, 211, 211, 255),
    'lightgreen': (144, 238, 144, 255),
    'lightgrey': (211, 211, 211, 255),
    'lightpink': (255, 182, 193, 255),
    'lightsalmon': (255, 160, 122, 255),
    'lightseagreen': (32, 178, 170, 255),
    'lightskyblue': (135, 206, 250, 255),
    'lightslategray': (119, 136, 153, 255),
    'lightslategrey': (119, 136, 153, 255),
    'lightsteelblue': (176, 196, 222, 255),
    'lightyellow': (255, 255, 224, 255),
    'lime': (0, 255, 0, 255),
    'limegreen': (50, 205, 50, 255),
    'linen': (250, 240, 230, 255),
    'magenta': (255, 0, 255, 255),
    'maroon': (128, 0, 0, 255),
    'mediumaquamarine': (102, 205, 170, 255),
    'mediumblue': (0, 0, 205, 255),
    'mediumorchid': (186, 85, 211, 255),
    'mediumpurple': (147, 112, 219, 255),
    'mediumseagreen': (60, 179, 113, 255),
    'mediumslateblue': (123, 104, 238, 255),
    'mediumspringgreen': (0, 250, 154, 255),
    'mediumturquoise': (72, 209, 204, 255),
    'mediumvioletred': (199, 21, 133, 255),
    'midnightblue': (25, 25, 112, 255),
    'mintcream': (245, 255, 250, 255),
    'mistyrose': (255, 228, 225, 255),
    'moccasin': (255, 228, 181, 255),
    'navajowhite': (255, 222, 173, 255),
    'navy': (0, 0, 128, 255),
    'oldlace': (253, 245, 230, 255),
    'olive': (128, 128, 0, 255),
    'olivedrab': (107, 142, 35, 255),
    'orange': (255, 165, 0, 255),
    'orangered': (255, 69, 0, 255),
    'orchid': (218, 112, 214, 255),
    'palegoldenrod': (238, 232, 170, 255),
    'palegreen': (152, 251, 152, 255),
    'paleturquoise': (175, 238, 238, 255),
    'palevioletred': (219, 112, 147, 255),
    'papayawhip': (255, 239, 213, 255),
    'peachpuff': (255, 218, 185, 255),
    'peru': (205, 133, 63, 255),
    'pink': (255, 192, 203, 255),
    'plum': (221, 160, 221, 255),
    'powderblue': (176, 224, 230, 255),
    'purple': (128, 0, 128, 255),
    'rebeccapurple': (102, 51, 153, 255),
    'red': (255, 0, 0, 255),
    'rosybrown': (188, 143, 143, 255),
    'royalblue': (65, 105, 225, 255),
    'saddlebrown': (139, 69, 19, 255),
    'salmon': (250, 128, 114, 255),
    'sandybrown': (244, 164, 96, 255),
    'seagreen': (46, 139, 87, 255),
    'seashell': (255, 245, 238, 255),
    'sienna': (160, 82, 45, 255),
    'silver': (192, 192, 192, 255),
    'skyblue': (135, 206, 235, 255),
    'slateblue': (106, 90, 205, 255),
    'slategray': (112, 128, 144, 255),
    'slategrey': (112, 128, 144, 255),
    'snow': (255, 250, 250, 255),
    'springgreen': (0, 255, 127, 255),
    'steelblue': (70, 130, 180, 255),
    'tan': (210, 180, 140, 255),
    'teal': (0, 128, 128, 255),
    'thistle': (216, 191, 216, 255),
    'tomato': (255, 99, 71, 255),
    'turquoise': (64, 224, 208, 255),
    'violet': (238, 130, 238, 255),
    'wheat': (245, 222, 179, 255),
    'white': (255, 255, 255, 255),
    'whitesmoke': (245, 245, 245, 255),
    'yellow': (255, 255, 0, 255),
    'yellowgreen': (154, 205, 50, 255),

    'transparent': (255, 255, 255, 0),
    'none': (0, 0, 0, 0)
}


NUM_ROUND = 3


def _clamp(low: int, value: int, high: int) -> int:
    return max(low, min(high, value))


def _clamp_tuple(low: int, values: Tuple[int, ...], high: int) -> Tuple[int, ...]:
    return tuple(_clamp(low, v, high) for v in values)


class Color:
    """
    Класс для представления и преобразования цвета с поддержкой различных моделей
    и форматов: RGB, RGBA, HEX, CMYK, HSL, HSV, CSS имена.
    """
    def __init__(self, r: Optional[Union[int, float]] = None, g: Optional[Union[int, float]] = None,
                 b: Optional[Union[int, float]] = None, a: Optional[Union[int, float]] = None):
        r, g, b = (int(round(v)) if v is not None else 0 for v in (r, g, b))
        a = int(round(a)) if a is not None else 255
        self._r, self._g, self._b, self._a = _clamp_tuple(0, (r, g, b, a), 255)

    @classmethod
    def from_random(cls, alpha: bool = False) -> 'Color':
        """Создать случайный цвет, альфа-прозрачность включительно если alpha=True."""
        return cls(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255) if alpha else 255)

    @classmethod
    def from_dict(cls, color: Dict[str, Union[int, float]]) -> 'Color':
        r = color.get('r', 0)
        g = color.get('g', 0)
        b = color.get('b', 0)
        a = color.get('a', 255)
        return cls(r, g, b, a)

    def to_dict(self) -> Dict[str, int]:
        return {'r': self._r, 'g': self._g, 'b': self._b, 'a': self._a}

    @classmethod
    def from_rgb(cls, color: Tuple[int, int, int]) -> 'Color':
        """Создать цвет из кортежа RGB."""
        return cls(*_clamp_tuple(0, color, 255))

    @classmethod
    def from_rgba(cls, color: Tuple[int, int, int, int]) -> 'Color':
        """Создать цвет из кортежа RGBA."""
        return cls(*_clamp_tuple(0, color, 255))

    @classmethod
    def from_hex(cls, color: str) -> 'Color':
        """Создать цвет из HEX-строки вида #RGB, #RGBA, #RRGGBB или #RRGGBBAA."""
        color = color.strip()

        pattern = r'^#?([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$'
        match = re.fullmatch(pattern, color)
        if not match:
            return cls()

        values = match.group(1)

        if len(values) in (3, 4):
            values = ''.join(ch * 2 for ch in values)

        r, g, b = int(values[0:2], 16), int(values[2:4], 16), int(values[4:6], 16)
        a = int(values[6:8], 16) if len(values) == 8 else 255

        return cls(*_clamp_tuple(0, (r, g, b, a), 255))

    @classmethod
    def from_css_name(cls, name: str) -> 'Color':
        """Создать цвет из CSS-имени, если не найдено — возвращается черный."""
        if name.lower() in css_named_colors:
            return cls(*css_named_colors[name.lower()])
        return cls()

    @classmethod
    def from_cmyk(cls, color: Tuple[int, int, int, int]) -> 'Color':
        """Создать цвет из CMYK (значения в процентах 0..100)."""
        c, m, y, k = (v / 100 for v in _clamp_tuple(0, color, 100))
        r = round(255 * (1 - c) * (1 - k))
        g = round(255 * (1 - m) * (1 - k))
        b = round(255 * (1 - y) * (1 - k))
        return cls(r, g, b)

    @classmethod
    def from_hsl(cls, color: Tuple[int, int, int]) -> 'Color':
        """Создать цвет из HSL (h: 0..360; s, l: 0..100)."""
        h, s, l = color
        h = _clamp(0, h, 360)
        s = _clamp(0, s, 100)
        l = _clamp(0, l, 100)

        s /= 100
        l /= 100
        c = (1 - abs(2 * l - 1)) * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = l - c / 2

        if h < 60:
            r, g, b = c, x, 0
        elif h < 120:
            r, g, b = x, c, 0
        elif h < 180:
            r, g, b = 0, c, x
        elif h < 240:
            r, g, b = 0, x, c
        elif h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x

        r, g, b = [(val + m) * 255 for val in (r, g, b)]
        return cls(r, g, b)

    @classmethod
    def from_hsv(cls, color: Tuple[int, int, int]) -> 'Color':
        """Создать цвет из HSV (h: 0..360; s, v: 0..100)."""
        h, s, v = color
        h = _clamp(0, h, 360)
        s = _clamp(0, s, 100)
        v = _clamp(0, v, 100)

        s /= 100
        v /= 100
        c = v * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = v - c

        if h < 60:
            r, g, b = c, x, 0
        elif h < 120:
            r, g, b = x, c, 0
        elif h < 180:
            r, g, b = 0, c, x
        elif h < 240:
            r, g, b = 0, x, c
        elif h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x

        r, g, b = [(val + m) * 255 for val in (r, g, b)]
        return cls(r, g, b)

    @property
    def rgb(self) -> Tuple[int, int, int]:
        return self._r, self._g, self._b

    @property
    def rgba(self) -> Tuple[int, int, int, int]:
        return self._r, self._g, self._b, self._a

    @property
    def _rgba_normalize(self) -> Tuple[float, float, float, float]:
        return self._r / 255, self._g / 255, self._b / 255, self._a / 255

    @property
    def hex(self) -> str:
        return f'#{self._r:02X}{self._g:02X}{self._b:02X}'

    @property
    def hexa(self) -> str:
        return f'#{self._r:02X}{self._g:02X}{self._b:02X}{self._a:02X}'

    @property
    def css_name(self) -> str:
        """Ближайшее CSS имя цвета по Евклидову расстоянию в RGBA."""
        def distance_to(_r: int, _g: int, _b: int, _a: int) -> float:
            return sqrt((_r - self._r) ** 2 + (_g - self._g) ** 2 + (_b - self._b) ** 2 + (_a - self._a) ** 2)

        for name, (r, g, b, a) in css_named_colors.items():
            if (r, g, b, a) == (self._r, self._g, self._b, self._a):
                return name

        closest_name = None
        min_distance = float('inf')

        for name, (r, g, b, a) in css_named_colors.items():
            dist = distance_to(r, g, b, a)
            if dist < min_distance:
                min_distance = dist
                closest_name = name
        return closest_name

    @property
    def cmyk(self) -> Tuple[int, int, int, int]:
        r, g, b, _ = self._rgba_normalize
        k = 1 - max(r, g, b)
        if k < 1:
            c = (1 - r - k) / (1 - k)
            m = (1 - g - k) / (1 - k)
            y = (1 - b - k) / (1 - k)
        else:
            c, m, y = 0, 0, 0
        return round(c * 100), round(m * 100), round(y * 100), round(k * 100)

    @property
    def brightness(self) -> float:
        value = 0.299 * self._r + 0.587 * self._g + 0.114 * self._b
        return value

    @property
    def hue(self) -> float:
        r, g, b, _ = self._rgba_normalize
        max_c, min_c = max(r, g, b), min(r, g, b)
        delta = max_c - min_c

        if delta == 0:
            value = 0.0
        elif max_c == r:
            value = ((g - b) / delta) % 6
        elif max_c == g:
            value = ((b - r) / delta) + 2
        else:
            value = ((r - g) / delta) + 4

        value *= 60
        if value < 0:
            value += 360
        return value

    @property
    def saturation(self) -> float:
        r, g, b, _ = self._rgba_normalize
        max_c, min_c = max(r, g, b), min(r, g, b)
        l = (max_c + min_c) / 2
        delta = max_c - min_c

        if delta == 0:
            value = 0.0
        else:
            value = delta / (1 - abs(2 * l - 1))
        return value

    @property
    def lightness(self) -> float:
        r, g, b, _ = self._rgba_normalize
        value = (max(r, g, b) + min(r, g, b)) / 2
        return value

    @property
    def hsv(self) -> Tuple[int, int, int]:
        r, g, b, _ = self._rgba_normalize
        max_c, min_c = max(r, g, b), min(r, g, b)
        delta = max_c - min_c

        h = self.hue

        v = max_c
        s = 0 if max_c == 0 else delta / max_c

        return round(h), round(s * 100), round(v * 100)

    @property
    def hsl(self) -> Tuple[int, int, int]:
        h = self.hue
        s = self.saturation
        l = self.lightness

        return round(h), round(s * 100), round(l * 100)

    def __add__(self, other: Union['Color', int,  float]) -> 'Color':
        if isinstance(other, Color):
            r = _clamp(0, self._r + other._r, 255)
            g = _clamp(0, self._g + other._g, 255)
            b = _clamp(0, self._b + other._b, 255)
            a = _clamp(0, self._a + other._a, 255)
        elif isinstance(other, (int, float)):
            r = _clamp(0, self._r + other, 255)
            g = _clamp(0, self._g + other, 255)
            b = _clamp(0, self._b + other, 255)
            a = _clamp(0, self._a + other, 255)
        else:
            return NotImplemented
        return Color(r, g, b, a)

    def __radd__(self, other: Union['Color', int,  float]) -> 'Color':
        if isinstance(other, Color):
            r = _clamp(0, other._r + self._r, 255)
            g = _clamp(0, other._g + self._g, 255)
            b = _clamp(0, other._b + self._b, 255)
            a = _clamp(0, other._a + self._a, 255)
        elif isinstance(other, (int, float)):
            r = _clamp(0, other + self._r, 255)
            g = _clamp(0, other + self._g, 255)
            b = _clamp(0, other + self._b, 255)
            a = _clamp(0, other + self._a, 255)
        else:
            return NotImplemented
        return Color(r, g, b, a)

    def __sub__(self, other: Union['Color', int,  float]) -> 'Color':
        if isinstance(other, Color):
            r = _clamp(0, self._r - other._r, 255)
            g = _clamp(0, self._g - other._g, 255)
            b = _clamp(0, self._b - other._b, 255)
            a = _clamp(0, self._a - other._a, 255)
        elif isinstance(other, (int, float)):
            r = _clamp(0, self._r - other, 255)
            g = _clamp(0, self._g - other, 255)
            b = _clamp(0, self._b - other, 255)
            a = _clamp(0, self._a - other, 255)
        else:
            return NotImplemented
        return Color(r, g, b, a)

    def __rsub__(self, other: Union['Color', int,  float]) -> 'Color':
        if isinstance(other, Color):
            r = _clamp(0, other._r - self._r, 255)
            g = _clamp(0, other._g - self._g, 255)
            b = _clamp(0, other._b - self._b, 255)
            a = _clamp(0, other._a - self._a, 255)
        elif isinstance(other, (int, float)):
            r = _clamp(0, other - self._r, 255)
            g = _clamp(0, other - self._g, 255)
            b = _clamp(0, other - self._b, 255)
            a = _clamp(0, other - self._a, 255)
        else:
            return NotImplemented
        return Color(r, g, b, a)

    def __neg__(self) -> 'Color':
        return Color(
            _clamp(0, 255 - self._r, 255),
            _clamp(0, 255 - self._g, 255),
            _clamp(0, 255 - self._b, 255),
            _clamp(0, 255 - self._a, 255),
        )

    def __mul__(self, multiplier: Union[int, float]) -> 'Color':
        r = _clamp(0, int(self._r * multiplier), 255)
        g = _clamp(0, int(self._g * multiplier), 255)
        b = _clamp(0, int(self._b * multiplier), 255)
        a = _clamp(0, int(self._a * multiplier), 255)
        return Color(r, g, b, a)

    def __rmul__(self, multiplier: Union[int, float]) -> 'Color':
        return self.__mul__(multiplier)

    def __eq__(self, color: 'Color') -> bool:
        return (self._r == color._r and
                self._g == color._g and
                self._b == color._b and
                self._a == color._a)

    def __ne__(self, other: 'Color') -> bool:
        return not self.__eq__(other)

    def __str__(self):
        return self.hexa

    def __repr__(self):
        return f'Color{self.hexa}({self._r}, {self._g}, {self._b}, {self._a})'
