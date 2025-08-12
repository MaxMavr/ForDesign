from PIL import Image
from utils.config import INPUT_DIR


def input_img(filename: str) -> Image:
    return Image.open(INPUT_DIR / filename).convert('RGB')
