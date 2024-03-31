import cv2 as cv
import numpy as np

img = cv.imread('Images/cat_1.jpg')
#cv.imshow('Img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
#cv.imshow('Blank', blank)

mask = cv.circle(blank,
                 (img.shape[1] // 2, img.shape[0] // 2),
                 100,
                 255,
                 -1)
#cv.imshow('Mask', mask)

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -30, 60)
#cv.imshow('Translated', translated)

masked = cv.bitwise_and(translated, translated, mask=mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)