from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class SVGrect:
    x: Union[int, float]
    y: Union[int, float]
    width: Union[int, float]
    height: Union[int, float]
    fill: Optional[str] = None
    stroke: Optional[str] = None
    stroke_width: Optional[Union[int, float]] = None
    rx: Optional[Union[int, float]] = None
    ry: Optional[Union[int, float]] = None
    classes: Optional[str] = None

    @property
    def svg(self) -> str:
        attrs = [
            f'x="{self.x}"',
            f'y="{self.y}"',
            f'width="{self.width}"',
            f'height="{self.height}"',
        ]

        if self.fill:
            attrs.append(f'fill="{self.fill}"')

        if self.stroke:
            attrs.append(f'stroke="{self.stroke}"')

        if self.stroke_width:
            attrs.append(f'stroke-width="{self.stroke_width}"')

        if self.rx is not None and self.ry is not None:
            attrs.append(f'rx="{self.rx}"')
            attrs.append(f'ry="{self.ry}"')

        if self.classes:
            attrs.append(f'class="{self.classes}"')

        return f'<rect {" ".join(attrs)} />'


@dataclass
class SVGline:
    x1: Union[int, float]
    y1: Union[int, float]
    x2: Union[int, float]
    y2: Union[int, float]
    stroke: Optional[str] = None
    stroke_width: Optional[Union[int, float]] = None
    stroke_dasharray: Optional[str] = None
    classes: Optional[str] = None

    @property
    def svg(self) -> str:
        attrs = [
            f'x1="{self.x1}"',
            f'y1="{self.y1}"',
            f'x2="{self.x2}"',
            f'y2="{self.y2}"',
        ]

        if self.stroke:
            attrs.append(f'stroke="{self.stroke}"')

        if self.stroke_width:
            attrs.append(f'stroke-width="{self.stroke_width}"')

        if self.stroke_dasharray:
            attrs.append(f'stroke-dasharray="{self.stroke_dasharray}"')

        if self.classes:
            attrs.append(f'class="{self.classes}"')

        return f'<line {" ".join(attrs)} />'
