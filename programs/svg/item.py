from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class SVGrect:
    x: Union[int, float]
    y: Union[int, float]
    width: Union[int, float]
    height: Union[int, float]
    fill: str = "none"
    stroke: str = "black"
    stroke_width: int = 1
    rx: Optional[Union[int, float]] = None
    ry: Optional[Union[int, float]] = None

    @property
    def svg(self) -> str:
        rounded_corners = ""
        if self.rx is not None and self.ry is not None:
            rounded_corners = f' rx="{self.rx}" ry="{self.ry}"'
        return (
            f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}"'
            f' fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.stroke_width}"'
            f'{rounded_corners} />'
        )


@dataclass
class SVGline:
    x1: Union[int, float]
    y1: Union[int, float]
    x2: Union[int, float]
    y2: Union[int, float]
    stroke: str = "black"
    stroke_width: int = 1
    stroke_dasharray: Optional[str] = None

    @property
    def svg(self) -> str:
        dash_attr = ""
        if self.stroke_dasharray:
            dash_attr = f' stroke-dasharray="{self.stroke_dasharray}"'
        return (
            f'<line x1="{self.x1}" y1="{self.y1}" x2="{self.x2}" y2="{self.y2}"'
            f' stroke="{self.stroke}" stroke-width="{self.stroke_width}"{dash_attr} />'
        )
