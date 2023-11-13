from PIL import Image


def mirror():
    im = Image.open('image.jpg')
    pixels = im.load()  # список с пикселями
    x, y = im.size  # ширина (x) и высота (y) изображения
    for i in range(x):
        for j in range(x - 1):
            pixels[j, i], pixels[x - i - 1, x - j - 1] = \
                pixels[x - i - 1, x - j - 1], pixels[j, i]
    im.save('res.jpg')


mirror()
