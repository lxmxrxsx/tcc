import cv2 as cv
import numpy as np


def main():
    # carregando imagens
    mapImage = cv.imread(
        './images/bloons_mapa_com_macacos.png', cv.IMREAD_UNCHANGED)
    monkeyImage = cv.imread('./images/bloons_macaco.png', cv.IMREAD_UNCHANGED)
    path = "./images/find_all_monkeys.png"

    findOnImage(image=mapImage, object=monkeyImage, path=path)


def findOnImage(image, object, path, threshold=0.616, method=cv.TM_CCOEFF_NORMED,):
    # pegando dimensoes do projeto
    objectWidth = object.shape[1]
    objectHeight = object.shape[0]

    # resultado da leitura da imagem
    result = cv.matchTemplate(image, object, method)

    # salvando apenas as localizacoes com confianca maior que threshold
    locations = np.where(result > threshold)
    locations = list(zip(*locations[::-1]))

    # criando um array de retangulos e agrupando-os para remover os retangulos zoados
    # rectangle = [position x, position y, width, height]
    rectangles = []

    for rectangle in locations:
        rectangle = [int(rectangle[0]), int(rectangle[1]),
                     objectWidth, objectHeight]
        # adcionando duas vezes ao array para que quando aguapar os retangulos nenhum fique de fora
        rectangles.append(rectangle)
        rectangles.append(rectangle)

    rectangles = cv.groupRectangles(rectangles, 1, 0.2)

    if len(rectangles):
        # decompondo o retangulo no for para pegar os valores nominalmente
        for (x, y, width, height) in rectangles:
            imageTopLeft = (x, y)
            imageBottomRight = (
                x + width,
                y + height
            )
            # fazendo o retangulo em volta da imagem
            cv.rectangle(image, imageTopLeft, imageBottomRight,
                         color=(255, 0, 0), thickness=2, lineType=cv.LINE_4)

        cv.imshow('Window', image)
        cv.waitKey()
        # salvando imagem no path
        cv.imwrite(path, image)
    else:
        print('ih')
    return 0


main()
