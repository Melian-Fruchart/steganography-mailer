from random import randint
from PIL import Image

im = Image.open('./resources/images/cat1.jpg')
pixelMap = im.load()

img = Image.new(im.mode, im.size)
pixelsNew = img.load()

start_range = 0
end_range = 100
for i in range(img.size[0]):
    for j in range(img.size[1]):
        a, b, c, = randint(start_range, end_range), randint(start_range, end_range), randint(start_range, end_range)
        pixelsNew[i, j] = tuple(map(sum, zip(im.getpixel((i, j)), (a, b, c))))

im.close()
img.show()
img.save("./resources/output/output-cat1.jpg")
img.close()



def file_reader(file_input, buffer_size):
    with open(file_input, "r+b") as f:
        while chunk := f.read(buffer_size):
            yield chunk


cat1 = file_reader("./resources/images/cat1.jpg", 100)

