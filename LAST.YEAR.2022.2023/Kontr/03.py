from PIL import Image


def nothing_special(file_name, *coords, color):
    origenal_img = Image.open(file_name)
    pixels = origenal_img.load()
    width, height = origenal_img.size
    old_img = Image.new('RGB', (width, height), color)
    transform = 0
    for n in range(len(coords)):  # перебираем пары координат
        # выризаем
        x = coords[n][0]
        y = coords[n][1]
        xy_rect_to_crop = (x, y, x + 200, y + 200)  # x, y = левый верхний угол.  x + число правый нижний угол
        fragment = origenal_img.crop(xy_rect_to_crop)
        # выполняем трансформацию( меняем выризаную картинку)
        if transform == 0:
            pass
        elif transform == 1:
            fragment = fragment.transpose(Image.FLIP_LEFT_RIGHT)  # отражаем в доль вертикальной оси
        elif transform == 2:
            fragment = fragment.transpose(Image.FLIP_TOP_BOTTOM)  # отражаем в доль горизонтальной оси
        transform += 1
        if transform > 2:  # обнуляем
            transform = 0
        # вставка фразмента в итоговое изображение
        x = n * 200
        y = n * 200
        rect_to_paste = (x, y, x + 200, y + 200)
        old_img.paste(fragment, rect_to_paste)
    old_img.save('02.png')


nothing_special('01.png', (100, 250), (280, 550), (550, 50), (350, 0),
                color='#a6f6d6')
