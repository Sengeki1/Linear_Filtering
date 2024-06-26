import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Images/cat_1.jpg')
#cv.imshow('Image', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('HSV', hsv)

# BGR to LAD
lad = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow('LAD', lad)

# plt.imshow(img)
# plt.show()

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)