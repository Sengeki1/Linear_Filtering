import cv2 as cv
import numpy as np

img = cv.imread('Images/cat_1.jpg')
cv.imshow("Image", img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'Contours found: {len(contours)}')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)