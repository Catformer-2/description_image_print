import json
from PIL import Image

with open("waypoint.txt", "r") as f:
    waypoints = json.load(f)

initial_x = waypoints[0]["pos"]["x"]
initial_z = waypoints[0]["pos"]["z"]


image = Image.open("input.png")
image = image.convert("RGBA")
width, height = image.size
pixels = image.load()
new_waypoints = []

for y in range(height):
    for x in range(width):
        pixel = pixels[x, y]
        if len(pixel) == 3:
            r, g, b = pixel
            a = 255
        else:
            r, g, b, a = pixel

        argb_color = (a << 24) | (r << 16) | (g << 8) | b
        decimal_color = argb_color if argb_color >= 0 else argb_color + 2**32

        new_waypoint = {
            "time": waypoints[0]["time"],
            "name": f"{waypoints[0]['name']}_{y * width + x}",
            "pos": {
                "x": initial_x + x,
                "y": waypoints[0]["pos"]["y"],
                "z": initial_z - (height - 1 - y)
            },
            "color": decimal_color,
            "icon_index": waypoints[0]["icon_index"],
            "can_position_float": waypoints[0]["can_position_float"],
            "type": waypoints[0]["type"]
        }

        new_waypoints.append(new_waypoint)

with open("output_waypoints.txt", "w") as f:
    json.dump(new_waypoints, f, separators=(",", ":"))
