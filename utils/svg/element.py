from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from typing import Optional, Union, Dict, List
from utils.color import Color


@dataclass
class SVGElement(ABC):
    @property
    @abstractmethod
    def svg(self) -> str:
        ...

    @staticmethod
    def _attrs_to_str(attrs: Dict[str, Optional[Union[str, float]]]) -> str:
        return " ".join(f'{k}="{v}"' for k, v in attrs.items() if v is not None)

    def __str__(self) -> str:
        return self.svg


@dataclass
class SVGrect(SVGElement):
    x: Union[int, float]
    y: Union[int, float]
    width: Union[int, float]
    height: Union[int, float]
    fill: Optional[Color] = None
    stroke: Optional[Color] = None
    stroke_width: Optional[Union[int, float]] = None
    rx: Optional[Union[int, float]] = None
    ry: Optional[Union[int, float]] = None
    classes: Optional[str] = None

    @property
    def svg(self) -> str:
        attrs = {
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'fill': self.height,
            'stroke': self.height,
            'stroke-width': self.height,
            'rx': self.rx,
            'ry': self.ry,
            'class': self.classes,
        }

        if self.rx is not None and self.ry is not None:
            attrs["rx"] = str(self.rx)
            attrs["ry"] = str(self.ry)

        return f'<rect {self._attrs_to_str(attrs)} />'


@dataclass
class SVGline(SVGElement):
    x1: Union[int, float]
    y1: Union[int, float]
    x2: Union[int, float]
    y2: Union[int, float]
    stroke: Optional[Color] = None
    stroke_width: Optional[Union[int, float]] = None
    stroke_dasharray: Optional[str] = None
    classes: Optional[str] = None

    @property
    def svg(self) -> str:
        attrs = {
            'x1': self.x1,
            'y1': self.y1,
            'x2': self.x2,
            'y2': self.y2,
            'stroke': str(self.stroke),
            'stroke-width': self.stroke_width,
            'stroke-dasharray': self.stroke_dasharray,
            'class': self.classes
        }

        return f'<line {self._attrs_to_str(attrs)} />'


@dataclass
class SVGGroup(SVGElement):
    elements: List[SVGElement] = field(default_factory=list)
    classes: Optional[str] = None

    @property
    def svg(self) -> str:
        content = '\n'.join(element.svg for element in self.elements)
        class_attr = f' class="{self.classes}"' if self.classes else ""
        return f'<g{class_attr}>\n{content}\n</g>'


@dataclass
class GradientLine(SVGline):
    color1: Optional[Color] = None
    color2: Optional[Color] = None

    def invert(self) -> 'GradientLine':
        return GradientLine(
            x1=self.x1,
            y1=self.y1,
            x2=self.x2,
            y2=self.y2,
            stroke=self.stroke,
            stroke_width=self.stroke_width,
            stroke_dasharray=self.stroke_dasharray,
            classes=self.classes,
            color1=self.color2,
            color2=self.color1
        )

    def value(self, x: int, y: int) -> float:
        dx, dy = self.x2 - self.x1, self.y2 - self.y1
        if dx == dy == 0:
            return 0
        t = ((x - self.x1) * dx + (y - self.y1) * dy) / (dx * dx + dy * dy)
        return max(0.0, min(1.0, t))

    def color(self, x: int, y: int) -> Optional[Color]:
        t = self.value(x, y)
        if self.color1 and self.color2:
            return self.color1 * (1 - t) + self.color2 * t
        return self.color1 or self.color2
