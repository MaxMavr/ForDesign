from utils.system import file
from color import Color
from utils import svg
from utils.svg.element import SVGrect
from utils.img import input_img


def colorful(filename: str):
    img = input_img(filename)
    name = file.split_filename(filename, 'n')

    styles_dict = dict()
    styles = []
    rects = []

    for y in range(img.height):
        for x in range(img.width):
            color = Color.from_rgb(img.getpixel((x, y))).hex

            if color not in styles_dict:
                styles_dict[color] = len(styles_dict) + 1
                styles.append(f'.st{styles_dict[color]}{{fill:{color};}}')

            rects.append(SVGrect(x, y, 1, 1, classes=f'st{styles_dict[color]}'))

    svg.make(
        width=img.width,
        height=img.height,
        styles=styles,
        content=rects,
        filename=name,
        attributes={"shape-rendering": "crispEdges"}
    )


def monochrome(filename: str, target_color: Color = Color()):
    img = input_img(filename)
    name = file.split_filename(filename, 'n')

    rects = []

    for y in range(img.height):
        for x in range(img.width):
            color = Color.from_rgb(img.getpixel((x, y)))

            if color == target_color:
                rects.append(SVGrect(x, y, 1, 1, classes='st').svg)

    svg.make(
        width=img.width,
        height=img.height,
        styles=[f'.st{{fill:{target_color.hex};}}'],
        content=rects,
        filename=name,
        attributes={"shape-rendering": "crispEdges"})


if __name__ == '__main__':
    monochrome('brick.png', Color.from_hex('#B1624D'))
    colorful('brick.png')
