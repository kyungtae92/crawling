import cv2
import numpy as np

#                     # 가로 세로
# image = np.full((480, 640, 3), 255, np.uint8)
# cv2.imshow('white', image)
# cv2.waitKey()
# cv2.destroyAllWindows()

#                                 # RGB BGR
# image = np.full((480, 640, 3), (0, 0, 255), np.uint8)
# cv2.imshow('red', image)
# cv2.waitKey()
# cv2.destroyAllWindows()


image[240, 160] = image[240, 320] = image[240, 480] = (255, 255, 255)
cv2.imshow('black with white pixels', image)
cv2.waitKey()
cv2.destroyAllWindows()


# image = cv2.imread('C:/Python Projects/crawling/lena.png')
# image = image.astype(np.float32) / 255
# print("Shape:", image.shape)
# print("Data type:", image.dtype)
#
# cv2.imshow('image', np.clip(image*2, 0, 1))
# cv2.imshow('image', image)
# cv2.waitKey()
# cv2.destroyAllWindows()


# image = cv2.imread('C:/Python Projects/crawling/lena.png')
# image = image.astype(np.float32) / 255
# print("Shape:", image.shape)
# print("Data type:", image.dtype)
# image[:,:,[0,2]] = image[:,:,[2,0]]
# cv2.imshow('image', image)
# cv2.waitKey()
# cv2.destroyAllWindows()

#
# image = cv2.imread('C:\Python Projects\crawling/lena.png')
# image = image.astype(np.float32) / 255
# print("Shape:", image.shape)
# print("Data type:", image.dtype)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('image', gray)
# cv2.waitKey()
# cv2.destroyAllWindows()


# image = cv2.imread('C:/Python Projects/crawling/lena.png')
# image = image.astype(np.float32) / 255
# print("Shape:", image.shape)
# print("Data type:", image.dtype)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imshow('image', gray)
# cv2.waitKey()
# cv2.destroyAllWindows()


# image = cv2.imread('C:/Python Projects/crawling/lena.png',0)
# image = image.astype(np.float32) / 255
#
# gamma = 0.3
# corrected_image = np.power(image, gamma)
#
# cv2.imshow('image', image)
# cv2.imshow('corrected_image', corrected_image)
# cv2.waitKey()
# cv2.destroyAllWindows()