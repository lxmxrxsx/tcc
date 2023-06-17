import cv2 as cv
import numpy as np
import image as img
import preprocessing

height = 500
width = 500
w0 = 480
h0 = 420

binary = preprocessing.main()

andImage = cv.imread('./images/maps/aaaa.jpeg')


andImage[h0, w0] = [255, 255, 255]


print(andImage[h0, w0])

cv.imwrite('circulinho.png', andImage)
