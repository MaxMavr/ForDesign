from programs.system import file
from programs.color.decoding import rgb2hex
from PIL import Image
from programs import svg
import os.path


def colorful(namefile: str):
    img = Image.open(f'input/{namefile}').convert('RGB')
    name = file.split_filename(namefile, 'n')

    styles_dict = dict()
    styles = []
    rects = []

    for y in range(img.height):
        for x in range(img.width):
            color = rgb2hex(img.getpixel((x, y)))

            if color not in styles_dict:
                styles_dict[color] = len(styles_dict) + 1
                styles.append(f'.st{styles_dict[color]}{{fill:{color};}}')

            rects.append(f'<rect class="st{styles_dict[color]}" x="{x}" y="{y}" width="1" height="1"/>')

    svg.make(
        width=img.width,
        height=img.height,
        styles=styles,
        content=rects,
        output_path=os.path.join(os.path.dirname(__file__), "output", f"{name}.svg"),
        attributes={"shape-rendering": "crispEdges"}
    )


def monochrome(namefile: str, target_color: str = '#000000'):
    img = Image.open(f'input/{namefile}').convert('RGB')
    name = file.split_filename(namefile, 'n')

    rects = []

    for y in range(img.height):
        for x in range(img.width):
            color = rgb2hex(img.getpixel((x, y)))

            if color == target_color:
                rects.append(f'<rect x="{x}" y="{y}" width="1" height="1"/>')

    svg.make(
        width=img.width,
        height=img.height,
        styles=None,
        content=rects,
        output_path=os.path.join(os.path.dirname(__file__), "output", f"{name}.svg"),
        attributes={"shape-rendering": "crispEdges"})


if __name__ == '__main__':
    colorful('test.png')
    # monochrome('Плакат-узор.gif')
    # monochrome('Плакат-узор.gif')
    # monochrome('Плакат-шум.gif')
