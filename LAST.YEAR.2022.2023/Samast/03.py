from PIL import Image, ImageDraw


def oyster(filename, w, *colors):
    im = Image.new("RGB", (7 * w, 5 * w), (255, 255, 255))
    drawer = ImageDraw.Draw(im)
    ystriza, chemch, taibl = colors
    drawer.rectangle((0, int(2.5 * w), int(7 * w), int(5 * w)), taibl)
    im.save(filename)


oyster('img.png', 40, '#A5A5A5', '#FFFAFA', '#A85F2E')
