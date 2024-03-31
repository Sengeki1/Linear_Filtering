import cv2 as cv

img = cv.imread('Images/cat_1.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
# it looks at the image compares each pixel value to this threshold value
# and if it is above this value it sets it to 255 otherwise it infers that
# if it falls bellow it sets it to zero.
cv.imshow('Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Threshold_Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray
                                       , 255
                                       , cv.ADAPTIVE_THRESH_MEAN_C
                                       , cv.THRESH_BINARY
                                       , 11
                                       , 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)