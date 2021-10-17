from colormath.color_objects import sRGBColor
from colr import Colr as C

color_dict = {
    "1d1f21": "base00-hex",
    "282a2e": "base01-hex",
    "373b41": "base02-hex",
    "969896": "base03-hex",
    "b4b7b4": "base04-hex",
    "c5c8cf": "base05-hex",
    "e0e0e0": "base06-hex",
    "ffffff": "base07-hex",
    "cc6666": "base08-hex",
    "de935f": "base09-hex",
    "f0c674": "base0A-hex",
    "b5bd68": "base0B-hex",
    "8abeb7": "base0C-hex",
    "81a2be": "base0D-hex",
    "b294bb": "base0E-hex",
    "a3685a": "base0F-hex",
}

def color_pick():
    print("Convert color")
    colors = [sRGBColor.new_from_rgb_hex(color) for color in list(color_dict.keys()) ]
    for color in colors:
        c = color.get_upscaled_value_tuple()
        C(text= "  ").b_rgb(c[0], c[1], c[2]).print()

if __name__ == "__main__":
    color_pick()
