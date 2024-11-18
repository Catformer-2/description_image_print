import json
from PIL import Image

sel_character = ":::::"
image = Image.open("input.png")
image = image.convert("RGBA")
width, height = image.size
pixels = image.load()
new_waypoints = []

for y in range(height):
    new_waypoints.append("\n")
    for x in range(width):
        pixel = pixels[x, y]
        if len(pixel) == 3:
            r, g, b = pixel
            a = 255
        else:
            r, g, b, a = pixel

        new_waypoint = rgb_to_hex(r, g, b) + sel_character
        new_waypoints.append(new_waypoint)

with open('Description.txt', 'w') as f:
    for line in new_waypoints:
        f.write(f"{line}")
