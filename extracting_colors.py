from colorthief import ColorThief

color_thief = ColorThief('input.png')

dominant_color = color_thief.get_color(quality=1)
palette = color_thief.get_palette(color_count=10)

print(palette)