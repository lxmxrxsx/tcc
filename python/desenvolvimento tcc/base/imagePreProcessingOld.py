import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# img = cv.imread(
#     './images/maps/beginner/map_monkey_meadow.png')

img = cv.imread('../testImages/Screenshot_1.png')

imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

H, S, V = cv.split(imgHSV)

cv.imwrite('testImages/image.png', img)
cv.imwrite("testImages/HSV_image.png", imgHSV)
cv.imwrite("testImages/H_image.png", H)


keys = plt.hist(H.ravel(), 180, [0, 180])[0]

print(len(keys))
min, max, minLoc, maxLoc = cv.minMaxLoc(keys)

maxPositionArray = np.where(keys == max)
maxPosition = maxPositionArray[0]
print(maxPosition)


# o que nao se encontra no range fica preto
# o que está no range fica branco
inRange = cv.inRange(H, maxPosition-4, maxPosition+4)

cv.imwrite("testImages/in_range_image.png", inRange)

inRangePath = cv.inRange(H, 30, 35)

cv.imwrite("testImages/in_range_path_image.png", inRangePath)

plt.hist(H.ravel(), 180, [0, 180])
plt.title("histograma H")
plt.savefig('hist.png')

# testes com filtros da canny

cv.imwrite("testImages/canny.png", cv.Canny(img, 70, 70))

cv.imwrite("testImages/canny_in_range.png", cv.Canny(inRange, 70, 70))

cv.imwrite("testImages/canny_path.png",
           cv.Canny(cv.inRange(H, 30, 35), 70, 70))

cv.imwrite("testImages/canny_H.png", cv.Canny(H, 70, 70))


# testes cp, filtro de cartoon

cv.imwrite("testImages/cartoon.png",
           cv.edgePreservingFilter(img, flags=1, sigma_s=50, sigma_r=0.4))

cv.imwrite("testImages/cartoon_in_range.png",
           cv.edgePreservingFilter(inRange, flags=1, sigma_s=50, sigma_r=0.4))

cv.imwrite("testImages/cartoon_path.png",
           cv.edgePreservingFilter(cv.inRange(H, 30, 35), flags=1, sigma_s=20, sigma_r=0.9))

cv.imwrite("testImages/cartoon_H.png",
           cv.edgePreservingFilter(H, flags=1, sigma_s=50, sigma_r=0.4))


element_str = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))


cv.imwrite("testImages/erode.png", cv.erode(img, element_str, iterations=2))

cv.imwrite("testImages/erode_in_range.png",
           cv.erode(inRange, element_str, iterations=2))

cv.imwrite("testImages/erode_path.png",
           cv.erode(cv.inRange(H, 30, 35), element_str, iterations=2))

cv.imwrite("testImages/erode_H.png", cv.erode(H, element_str, iterations=2))


# ax2 = fig.add_subplot(222)
# ax2.hist(S.ravel(), 256, [0, 256])
# plt.title("histograma S")

# ax3 = fig.add_subplot(223)
# ax3.hist(V.ravel(), 256, [0, 256])
# plt.title("histograma V")

# ax1 = fig.add_subplot(224)
# ax1.hist(imgGray.ravel(), 256, [0, 256])
# plt.title("histograma Cinza")

# plt.waitforbuttonpress()


# https://stackoverflow.com/questions/34712144/merge-hsv-channels-under-opencv-3-in-python
# S.fill(255)
# V.fill(255)
# hsv_image = cv.merge([H, S, V])

# out = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)

# cv.imshow('example', out)
# cv.waitKey()
