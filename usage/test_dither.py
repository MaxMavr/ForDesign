from utils.img import save_img, empty_img
from utils.color.dither import (pattern_dither_8x8,
                                pattern_dither_4x4,
                                noise_dither,
                                white_noise_dither,
                                threshold_dither,
                                clustered_dot_dither,
                                blue_noise_dither)
from utils.color.const import FIREBRICK, HOTPINK
from utils.svg.element import GradientLine


width = 1000
height = 1000

gradient_line = GradientLine(0, 0, width, height, color1=FIREBRICK, color2=HOTPINK)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        color = gradient_line.color(x, y)
        img.putpixel((x, y), color.rgb)
save_img(img, 'gradient_line', quiet=False)


img = empty_img((width, height))
invert_gradient_line = gradient_line.invert()
for y in range(height):
    for x in range(width):
        color = invert_gradient_line.color(x, y)
        img.putpixel((x, y), color.rgb)
save_img(img, 'invert_gradient_line', quiet=False)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        color = gradient_line.color(x, y)
        img.putpixel((x, y), color.rgb)
save_img(img, 'gradient_line', quiet=False)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        brightness = gradient_line.value(x, y)
        if pattern_dither_8x8(x, y, brightness):
            img.putpixel((x, y), gradient_line.color1.rgb)
        else:
            img.putpixel((x, y), gradient_line.color2.rgb)
save_img(img, 'pattern_dither_8x8', quiet=False)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        brightness = gradient_line.value(x, y)
        if pattern_dither_4x4(x, y, brightness):
            img.putpixel((x, y), gradient_line.color1.rgb)
        else:
            img.putpixel((x, y), gradient_line.color2.rgb)
save_img(img, 'pattern_dither_4x4', quiet=False)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        brightness = gradient_line.value(x, y)
        if noise_dither(brightness):
            img.putpixel((x, y), gradient_line.color1.rgb)
        else:
            img.putpixel((x, y), gradient_line.color2.rgb)
save_img(img, 'noise_dither', quiet=False)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        brightness = gradient_line.value(x, y)
        if white_noise_dither(brightness, 0.1):
            img.putpixel((x, y), gradient_line.color1.rgb)
        else:
            img.putpixel((x, y), gradient_line.color2.rgb)
save_img(img, 'white_noise_dither_10', quiet=False)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        brightness = gradient_line.value(x, y)
        if white_noise_dither(brightness, 0.15):
            img.putpixel((x, y), gradient_line.color1.rgb)
        else:
            img.putpixel((x, y), gradient_line.color2.rgb)
save_img(img, 'white_noise_dither_15', quiet=False)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        brightness = gradient_line.value(x, y)
        if white_noise_dither(brightness, 0.2):
            img.putpixel((x, y), gradient_line.color1.rgb)
        else:
            img.putpixel((x, y), gradient_line.color2.rgb)
save_img(img, 'white_noise_dither_20', quiet=False)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        brightness = gradient_line.value(x, y)
        if white_noise_dither(brightness, 0.3):
            img.putpixel((x, y), gradient_line.color1.rgb)
        else:
            img.putpixel((x, y), gradient_line.color2.rgb)
save_img(img, 'white_noise_dither_30', quiet=False)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        brightness = gradient_line.value(x, y)
        if white_noise_dither(brightness, 0.5):
            img.putpixel((x, y), gradient_line.color1.rgb)
        else:
            img.putpixel((x, y), gradient_line.color2.rgb)
save_img(img, 'white_noise_dither_50', quiet=False)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        brightness = gradient_line.value(x, y)
        if threshold_dither(brightness, 0.5):
            img.putpixel((x, y), gradient_line.color1.rgb)
        else:
            img.putpixel((x, y), gradient_line.color2.rgb)
save_img(img, 'threshold_dither_0,5', quiet=False)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        brightness = gradient_line.value(x, y)
        if clustered_dot_dither(x, y, brightness):
            img.putpixel((x, y), gradient_line.color1.rgb)
        else:
            img.putpixel((x, y), gradient_line.color2.rgb)
save_img(img, 'clustered_dot_dither', quiet=False)


img = empty_img((width, height))
for y in range(height):
    for x in range(width):
        brightness = gradient_line.value(x, y)
        if blue_noise_dither(x, y, brightness):
            img.putpixel((x, y), gradient_line.color1.rgb)
        else:
            img.putpixel((x, y), gradient_line.color2.rgb)
save_img(img, 'blue_noise_dither', quiet=False)
