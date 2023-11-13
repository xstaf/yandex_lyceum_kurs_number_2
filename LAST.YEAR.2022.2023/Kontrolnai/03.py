# Желания

from PIL import Image


def wayward(filename, one,ywe, color):
    # Открываем исходную картинку
    original_img = Image.open(filename)
    pixels = original_img.load()
    width, height = original_img.size
    # Создаём новый файл
    result_img = Image.new("RGB", (width, height), color)

    result_img.save("reflection.jpg")


wayward('mister.png', 300, 20, '#760606')
