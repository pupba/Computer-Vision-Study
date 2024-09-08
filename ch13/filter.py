from PIL import Image
from PIL import ImageFilter
image = Image.open("human.png")
blur = image.filter(ImageFilter.BLUR)
gaussian = image.filter(ImageFilter.GaussianBlur)

blur.show()
gaussian.show()