import cv2 as cv
from windowCapture import WindowCapture
from vision import Vision

windowCapture = WindowCapture()
visionMonkey = Vision('./images/chao_mapa_bloons.png')

while(True):

    screenshot = cv.imread(
        './images/maps/beginner/map_monkey_meadow.png', cv.IMREAD_UNCHANGED)

    cv.imwrite('retorno_identificacao_fundo.png',
               visionMonkey.find(screenshot, 0.55, 'rectangles'))

    break
    # if cv.waitKey(1) == ord('q'):
    #     cv.destroyAllWindows()
    #     print('done')
    #     break
