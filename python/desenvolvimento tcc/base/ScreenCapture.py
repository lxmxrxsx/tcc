from time import time
import numpy as np
import cv2 as cv
import pyautogui

loopTime = time()
while(True):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1 / (time() - loopTime)))
    loopTime = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        print('done')
        break
