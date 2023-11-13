from PIL import Image, ImageDraw


def oyster(filename, w, *colors):
    im = Image.new("RGB", (7 * w, 5 * w), (255, 255, 255))
    drawer = ImageDraw.Draw(im)
    ystriza, chemch, taibl = colors
    drawer.rectangle((0, int(2.5 * w), int(7 * w), int(5 * w)), taibl)
    drawer.ellipse((w, 2.5 * w, int(6 * w), int(4.5 * w)), ystriza)
    drawer.ellipse((int(1.5 * w), 0, int(6.5 * w), int(2.5 * w)), ystriza)
    drawer.ellipse((int(3 * w), int(2.5 * w), int(4 * w), int(3.5 * w)), chemch)

    im.save(filename)


oyster('img.png', 40, '#A5A5A5', '#FFFAFA', '#A85F2E')
