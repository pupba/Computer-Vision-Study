import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image

def image_to_vector(image_path):
    image = Image.open(image_path).convert('L')  # 흑백 이미지로 변환
    image = image.resize((100, 100))  # 크기 조정
    return np.array(image).flatten()  # 1차원 배열로 변환

# 이미지 경로
image1_path = 'cat1.jpg'
# image2_path = 'cat2.jpg'
image2_path = 'dog1.jpg'

# 이미지 벡터화
vector1 = image_to_vector(image1_path)
vector2 = image_to_vector(image2_path)

# 코사인 유사도 계산
similarity = cosine_similarity([vector1], [vector2])
print(f"Cosine Similarity: {similarity[0][0]}")
