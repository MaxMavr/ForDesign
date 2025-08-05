from PIL import Image
from math import sqrt
from programs.system.file import split_name_format
from pdf2image import convert_from_path
import cv2


w, b = (255, 255, 255, 255), (0, 0, 0, 255)  # Стандартные цвета (white, black)


def pdf2png(pdf_path, dpi: int = 300, save_img: str = None):  # size: Tuple[int, int]
    images = convert_from_path(pdf_path, dpi=dpi)

    if not save_img:
        save_img = f'{split_name_format(pdf_path, mode="n")}.png'

    if len(images) == 1:
        images[0].save('save_img', 'PNG')
        return

    for i, image in enumerate(images):
        image.save(f"{save_img}/page_{i + 1}.png", 'PNG')


def png2webp(png_img: str, quality: int = 100, save_img: str = None):
    if not save_img:
        save_img = f'{split_name_format(png_img, mode="n")}.webp'

    cv2.imwrite(
        save_img,
        cv2.imread(png_img, cv2.IMREAD_UNCHANGED),
        [int(cv2.IMWRITE_WEBP_QUALITY), quality]
    )


def percentage_of_black(img: str, show: bool = True):
    pic = Image.open(img)

    black_clr = 0
    rl_black_clr = 0
    white_clr = 0
    rl_white_clr = 0

    for x in range(pic.width):
        for y in range(pic.height):
            pixel_color = pic.getpixel((x, y))
            dist2b = sqrt((pixel_color[0] - b[0]) ** 2 + (pixel_color[1] - b[1]) ** 2 + (pixel_color[2] - b[2]) ** 2)
            dist2w = sqrt((pixel_color[0] - w[0]) ** 2 + (pixel_color[1] - w[1]) ** 2 + (pixel_color[2] - w[2]) ** 2)

            if dist2w > dist2b:
                rl_black_clr += 1
            else:
                rl_white_clr += 1

            if pixel_color == w:
                white_clr += 1

            if pixel_color == b:
                black_clr += 1

    if white_clr == 0:
        rl = '0%'
    else:
        rl = f'{round(black_clr * 100 / white_clr, 2)}%'

    if rl_white_clr == 0:
        rl_rl = '0%'
    else:
        rl_rl = f'{round(rl_black_clr * 100 / rl_white_clr, 2)}%'

    if show:
        print(f'\n{img}   {pic.width}x{pic.height}   {pic.width * pic.height}')
        print(f' {rl_rl.ljust(6)}   {str(rl_white_clr).ljust(5)} {str(rl_black_clr).ljust(5)}')
        print(f' {rl.ljust(6)}   {str(white_clr).ljust(5)} {str(black_clr).ljust(5)}')


if __name__ == "__main__":
    pdf2png('../Photo/TEST.pdf')
    # for i in range(10, 110, 10):
    #     png2webp('../Photo/butterfly-26.png', i, f'../Photo/butterfly-26({i}).webp')
