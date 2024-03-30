import cv2 as cv

img = cv.imread('Images/cat_1.jpg') # reads image
cv.imshow('Cat', img) # display image

def rescaleFrame(frame, scale=0.75):
    width= int(frame.shape[1] * scale) # width of image
    height = int(frame.shape[0] * scale) # height of image
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resizedImg = rescaleFrame(img)
cv.imshow('Image', resizedImg)

cv.waitKey(0) # key press wait time (infinite)