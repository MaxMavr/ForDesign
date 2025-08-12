from typing import Tuple
from utils.color import Color
from utils.color.const import WHITE
from PIL import Image
from utils.config import INPUT_DIR, OUTPUT_DIR
from utils.system.file import split_filename


def input_img(filename: str) -> Image:
    return Image.open(INPUT_DIR / filename).convert('RGB')


def empty_img(size: Tuple[int, int] = (300, 300), color: Color = WHITE) -> Image:
    return Image.new('RGB', size, color.rgb)


def save_img(img: Image, filename: str, quiet: bool = True) -> Image:
    name = split_filename(filename, 'n')
    output_path = OUTPUT_DIR / f'{name}.png'
    img.save(output_path, format='PNG')
    if not quiet:
        print(f'Сохранил {output_path}')
