import cv2 as cv
from windowCapture import WindowCapture
from vision import Vision

windowCapture = WindowCapture()
visionMonkey = Vision('./images/bloons_macaco.jpeg')

while(True):

    screenshot = windowCapture.get_screenshot()

    visionMonkey.find(screenshot, 0.6, 'rectangles')

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        print('done')
        break
