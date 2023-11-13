from PIL import Image, ImageDraw


def uguland_zapekanka(filename, w, *colors):
    im = Image.new("RGB", (10 * w, 6 * w), (255, 255, 255))
    drawer = ImageDraw.Draw(im)
    zapekanka, stone, plate = colors
    size = (0, 2 * w, 10 * w, 6 * w)
    drawer.ellipse(size, plate)
    drawer.rectangle(((int(1.5 * w)), w, 7 * w + int(1.5 * w), 4 * w), zapekanka)

    drawer.ellipse(((int(1.5 * w)), 0, 7 * w + int(1.5 * w), 2 * w), zapekanka)


    im.save(filename)


uguland_zapekanka('img.png', 40, '#95562D',
                  '#68736F', '#FFCC00')
