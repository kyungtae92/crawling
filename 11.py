import cv2
import numpy as np
import matplotlib.pyplot as plt

# image = cv2.imread('C:/Python Projects/crawling/lena.png', 0)
# image = image.astype(np.float32) / 255
#
# otsu_thr, otsu_mask = cv2.threshole(image, -1, 1, cv2, THRESH_BINARY | cv2.THRESH_OTSU)
#
# cv2.imshow('image', image)
# cv2.imshow('corrected_image', corrected_image)
# cv2.waitKey()
# cv2.destroyAllWindows()


image = cv2.imread('C:/Python Projects/crawling/lena.png', 0)
image = image.astype(np.float32)

otsu_thr, otsu_mask = cv2.threshold(image, -1, 1, cv2, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

plt.figure(figsize=(6, 3))
plt.subplot(121)
plt.axis('off')
plt.imshow(image, cmap='gray')
plt.subplot(122)
plt.axis('off')
plt.title('Otsu threshold')
plt.imshow(otsu_mask, crap='gray')
plt.tight_layout()
plt.show()

