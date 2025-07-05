from colorgram import extract

def extract_hirst_painting():
    colors = extract('hirst-painting.jpg', 60)
    colors_list = []
    for color in colors:
        colors_list.append((color.rgb[0], color.rgb[1], color.rgb[2]))
    return colors_list
