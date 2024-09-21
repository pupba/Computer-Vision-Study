import numpy as np
from PIL import Image

def image_to_binary_vector(image_path):
    image = Image.open(image_path).convert('1')  # 이진 이미지로 변환
    return np.array(image).flatten()  # 1차원 배열로 변환

# 이미지 경로
image1_path = 'cat1.jpg'
image2_path = 'dog1.jpg'

# 이진 이미지 벡터화
binary_vector1 = image_to_binary_vector(image1_path)
binary_vector2 = image_to_binary_vector(image2_path)

# 해밍 거리 계산
def hamming_distance(A, B):
    if len(A) != len(B):
        raise ValueError("두 벡터의 길이는 같아야 합니다.")
    return np.sum(A != B)

distance = hamming_distance(binary_vector1, binary_vector2)
print(f"Hamming Distance: {distance}")
