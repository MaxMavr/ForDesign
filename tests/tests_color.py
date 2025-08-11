from color import Color

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
clr.show_color()
