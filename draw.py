import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# Paint the image a certain colour
blank[200:300, 300:400] = 0, 255, 0

# Draw a rectangle
cv.rectangle(blank
             ,(0,0)
             ,(blank.shape[1] // 2, blank.shape[0] // 2)
             ,(255, 255, 0)
             ,thickness=cv.FILLED)

# Draw Circle
cv.circle(blank
          ,(blank.shape[1] // 2, blank.shape[0] // 2)
          , 40
          ,(0, 0,255)
          ,thickness=cv.FILLED)

# Draw Line
cv.line(blank, (0,0)
        ,(blank.shape[1] // 2, blank.shape[0] // 2)
        ,(255, 255, 255)
        ,thickness=3)

# Write text
cv.putText(blank
           ,"Hello"
           ,(255, 255)
           ,cv.FONT_HERSHEY_TRIPLEX # font
           ,1.0
           , (35, 155, 45)
           ,thickness=2)

cv.imshow('Image', blank)
cv.waitKey(0)