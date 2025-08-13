from utils.color import Color
from utils.color.operations import show_color, invert, complement, blend, grayscale, red_channel, green_channel, \
    blue_channel, alpha_channel, analogous, triad
from utils.img import input_img, save_img, empty_img
from utils.svg.element import GradientLine

clr = Color.from_hex('c1121f')

print(f'{clr.rgb = }')
print(f'{clr.rgba = }')
print(f'{clr.hex = }')
print(f'{clr.hexa = }')
print(f'{clr.css_name = }')
print(f'{clr.cmyk = }')
print(f'{clr.brightness = }')
print(f'{clr.hue = }')
print(f'{clr.saturation = }')
print(f'{clr.lightness = }')
print(f'{clr.hsv = }')
print(f'{clr.hsl = }')
print(f'{repr(clr) = }')
# show_color(clr)

img = input_img('photo_test_color.jpg')
gradient_line = GradientLine(0, 0, img.width, 0)


invert_colors_img = empty_img((img.width, img.height))
red_channel_img = empty_img((img.width, img.height))
green_channel_img = empty_img((img.width, img.height))
blue_channel_img = empty_img((img.width, img.height))
complement_img = empty_img((img.width, img.height))
blend_gradient_invert_img = empty_img((img.width, img.height))
blend_gradient_complement_img = empty_img((img.width, img.height))
add_complement_img = empty_img((img.width, img.height))
grayscale_img = empty_img((img.width, img.height))

triad1_img = empty_img((img.width, img.height))
triad2_img = empty_img((img.width, img.height))
analogous301_img = empty_img((img.width, img.height))
analogous302_img = empty_img((img.width, img.height))
analogous601_img = empty_img((img.width, img.height))
analogous602_img = empty_img((img.width, img.height))


for y in range(img.height):
    for x in range(img.width):
        color = Color.from_rgb(img.getpixel((x, y)))
        brightness = gradient_line.value(x, y)

        red_color = red_channel(color)
        red_channel_img.putpixel((x, y), red_color.rgb)
        green_color = green_channel(color)
        green_channel_img.putpixel((x, y), green_color.rgb)
        blue_color = blue_channel(color)
        blue_channel_img.putpixel((x, y), blue_color.rgb)

        invert_color = invert(color)
        invert_colors_img.putpixel((x, y), invert_color.rgb)
        complement_color = complement(color)
        complement_img.putpixel((x, y), complement_color.rgb)
        triad_color1, triad_color2 = triad(color)
        triad1_img.putpixel((x, y), triad_color1.rgb)
        triad2_img.putpixel((x, y), triad_color2.rgb)
        analogous30_color1, analogous30_color2 = analogous(color, 30)
        analogous301_img.putpixel((x, y), analogous30_color1.rgb)
        analogous302_img.putpixel((x, y), analogous30_color2.rgb)
        analogous60_color1, analogous60_color2 = analogous(color, 60)
        analogous601_img.putpixel((x, y), analogous60_color1.rgb)
        analogous602_img.putpixel((x, y), analogous60_color2.rgb)

        invert_color.a = brightness * 255
        blend_gradient_invert_img.putpixel((x, y), blend(invert_color, color).rgb)
        complement_color.a = brightness * 255
        blend_gradient_complement_img.putpixel((x, y), blend(complement_color, color).rgb)
        add_color = complement_color + color
        add_complement_img.putpixel((x, y), add_color.rgb)

        grayscale_img.putpixel((x, y), grayscale(color).rgb)

        offset = int(50 * math.sin(x / 10))
        new_color = shift_hue(color, offset)

save_img(red_channel_img, 'red_channel_img', quiet=False)
save_img(green_channel_img, 'green_channel_img', quiet=False)
save_img(blue_channel_img, 'blue_channel_img', quiet=False)

save_img(invert_colors_img, 'invert_colors_img', quiet=False)
save_img(complement_img, 'complement_img', quiet=False)
save_img(triad1_img, 'triad1_img', quiet=False)
save_img(triad2_img, 'triad2_img', quiet=False)
save_img(analogous301_img, 'analogous301_img', quiet=False)
save_img(analogous302_img, 'analogous302_img', quiet=False)
save_img(analogous601_img, 'analogous601_img', quiet=False)
save_img(analogous602_img, 'analogous602_img', quiet=False)

save_img(blend_gradient_invert_img, 'blend_gradient_invert_img', quiet=False)
save_img(blend_gradient_complement_img, 'blend_gradient_complement_img', quiet=False)
save_img(add_complement_img, 'add_complement_img', quiet=False)
save_img(grayscale_img, 'grayscale_img', quiet=False)





