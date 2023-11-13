from PIL import Image


def transparency(filename1, filename2):
    im1 = Image.open(filename1)
    im2 = Image.open(filename2)
    pixel1 = im1.load()
    pixel2 = im2.load()
    w, h = im1.size
    for x in range(w):
        for y in range(h):
            r0, g0, b0 = pixel1[x, y]
            r1, g1, b1 = pixel2[x, y]
            r = int(0.5 * r0 + 0.2 * r1)
            g = int(0.5 * g0 + 0.2 * g1)
            b = int(0.5 * b0 + 0.2 * b1)
            pixel1[x, y] = r, g, b
    im1.save('res.jpg')