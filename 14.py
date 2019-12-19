import cv2
import matplotlib.pyplot as plt
# 이미지를 불러옴
image = cv2.imread('C:/Python Projects/crawling/lena.png')
# canny알고리즘을 사용해 에지를 검출함
edges = cv2.Canny(image, 200, 100)
# 결과를 시각화함
plt.figure(figsize=(8,5))
plt.subplot(121)
plt.axis('off')
plt.title('original')
plt.imshow(image[:,:,[2,1,0]])
plt.subplot(122)
plt.axis('off')
plt.title('edges')
plt.imshow(edges, cmap='gray')
plt.tight_layout()
plt.show()