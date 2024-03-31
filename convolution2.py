import cv2
import numpy as np

def conv_transform(img):
    img_copy = img.copy()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_copy[i][j] = img[img.shape[0]-i-1][img.shape[1]-j-1] 
    return img_copy

def conv(img, kernel):
    # The img will be grayscale
    kernel = conv_transform(kernel)

    img_h = img.shape[0] 
    img_w = img.shape[1]

    kernel_h = img.shape[0] 
    kernel_w = img.shape[1]

    h = kernel_h//2 # to get integer value  
    w = kernel_w//2

    img_conv = np.zeros(img.shape)

    for i in range(h, img_h-h):
        for j in range(w, img_w-w):
            sum = 0

            for m in range(kernel_h):
                for n in range(kernel_w):
                    sum = sum + kernel[m][n] * img[i-h+m][j-w+n]

            img_conv[i][j] = sum

    #cv2.imshow('Convolved_img', img_conv)

    return img_conv

    #cv2.imwrite('/home/rafael2883/Pictures/img01.jpg', img_conv)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
