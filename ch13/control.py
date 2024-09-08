from PIL import Image

image = Image.open("human.png")
# 이미지 크기 조정(보간법 -> Image.Resampling.<보간법>)
re_img = image.resize(size=list(map(lambda x:int(x//2),list(image.size))),resample=Image.Resampling.LANCZOS)
re_img.show()
# 이미지 회전
rot_img = re_img.rotate(90)
rot_img.show()