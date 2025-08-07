from typing import List, Optional, Dict


def make(
        width: int,
        height: int,
        styles: Optional[List[str]],
        content: List[str],
        output_path: Optional[str] = None,
        attributes: Optional[Dict[str, str]] = None) -> str:

    if width <= 0 or height <= 0:
        raise ValueError("Ширина и высота должны быть целыми положительными числами")

    svg_attributes = {
        "xmlns": "http://www.w3.org/2000/svg",
        "viewBox": f"0 0 {width} {height}"
    }

    if attributes:
        svg_attributes.update(attributes)

    attributes_str = " ".join(f'{k}="{v}"' for k, v in svg_attributes.items())

    svg_content = [
        '<?xml version="1.0" encoding="utf-8"?>',
        f'<svg {attributes_str}>',
    ]

    if styles:
        svg_content.append('<style>')
        svg_content.extend(styles)
        svg_content.append('</style>')

    svg_content.extend(content)
    svg_content.append('</svg>')

    svg_str = '\n'.join(svg_content)

    if output_path is not None:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(svg_str)
    return svg_str
