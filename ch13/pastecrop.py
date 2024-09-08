from PIL import Image

# 배경 이미지
new = Image.new(mode="RGB",size=(1024,1024),color=(0,0,0))

# 붙여 넣을 이미지
image = Image.open("test2.png")

# 붙여 넣을 위치(x,y)
position = (0,0)

new.paste(image,position)
new.show()

# 자를 영역 지정(left, upper, right, lower)
crop_area = (100,100,400,400)
cropped_image = image.crop(crop_area)
cropped_image.show()