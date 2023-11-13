from PIL import Image

im = Image.open("image.jpg.")
pixels = im.load()  # список с пикселями
x, y = im.size  # ширина (x) и высота (y) изображения
rad = 0
green = 0
blye = 0
ra = []
gr = []
bl = []
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        ra.append(r)
        gr.append(g)
        bl.append(b)

        rad += r
        green += g
        blye += b
print(rad // len(ra), green // len(gr), blye // len(bl))
