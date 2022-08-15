import cv2 as cv
import numpy as np

# carregando imagens
mapImage = cv.imread(
    './images/bloons_mapa_com_macacos.png', cv.IMREAD_UNCHANGED)
monkeyImage = cv.imread('./images/bloons_macaco.png', cv.IMREAD_UNCHANGED)

# resultado da leitura da imagem
result = cv.matchTemplate(mapImage, monkeyImage, cv.TM_CCOEFF_NORMED)

# valores e posicao
minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)

# pegando largura e altura da imagem do mamaco
monkeyImageWidth = monkeyImage.shape[1]
monkeyImageHeight = monkeyImage.shape[0]

# definindo a parte superior esquerda e inferior direita
monkeyImagetopLeft = maxLoc
monkeyImageBottomRight = (
    monkeyImagetopLeft[0] + monkeyImageWidth,
    monkeyImagetopLeft[1] + monkeyImageHeight
)

# print posicao e confianca
print('best match top left position:', str(monkeyImagetopLeft))
print('best match confidence:', str(maxVal))

# fazendo o retangulo no mapa
cv.rectangle(mapImage, monkeyImagetopLeft, monkeyImageBottomRight,
             color=(255, 0, 0), thickness=2, lineType=cv.LINE_4)

# exibir imagem e esperar uma tecla para sair da tela
cv.imshow('most similar monkey', mapImage)
cv.waitKey()
# salvando imagem no arquivo 'identify_most_similar_image.png'
cv.imwrite("./images/identify_most_similar_image.png", mapImage)
