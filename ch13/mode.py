from PIL import Image

image = Image.open("test2.png")
print(image.mode) # RGB
print(image.convert("L").mode) # L(Grayscale)
print(image.convert("RGBA").mode) # RGBA(투명도 채널이 추가됨, 컬러값이 모두 0인 경우 투명)
print(image.convert("CMYK").mode) # CMYK(Cyan, Magenta, Yellow, Key(Black))
print(image.convert("1").mode) # 1-Bit Pixels (흑백 이미지를 비트 단위로 표현)