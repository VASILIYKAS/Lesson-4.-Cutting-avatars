from PIL import Image

# ~~~~~~~~~~ Стильная аватарка ~~~~~~~~~~
# Разделение картинки на каналы RGB
image = Image.open("monro.jpg") # <----- название любой картинки в папке
red, green, blue = image.split()

# Наложение со смещением красного канала
r_crop_coordinates = (30, 0, 696, 522) # Обрезаем слева 30 пикселей
r_cropped = red.crop(r_crop_coordinates)
r_crop_coordinates2 = (15, 0, 681, 522) # Обрезаем слева и справа по 15 пикселей
r_cropped2 = red.crop(r_crop_coordinates2)
r_image = Image.blend(r_cropped, r_cropped2, 0.5)

# Наложение со смещением синего канала
b_crop_coordinates = (0, 0, 666, 522) # Обрезаем справа 30 пикселей
b_cropped = blue.crop(b_crop_coordinates)
b_crop_coordinates2 = (15, 0, 681, 522) # Обрезаем слева и справа по 15 пикселей
b_cropped2 = blue.crop(b_crop_coordinates2)
b_image = Image.blend(b_cropped, b_cropped2, 0.5)

# Обрезка зеленого канала
g_crop_coordinates = (15, 0, 681, 522) # Обрезаем слева и справа по 15 пикселей
g_cropped = green.crop(g_crop_coordinates)

# Собираем всё вместе
new_image = Image.merge('RGB', (r_image, b_image, g_cropped))
new_image.save('final_monro.jpg')

# Финальная картинка обрезается до 80х63 (зависит от того сколько обрезали на
# этапе смещения каналов)
new_image.thumbnail((80, 80))
new_image.save('ava_monro.jpg')
