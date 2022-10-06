import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


def main():
    imagePath = getImage('monkey_meadow')
    image = readImage(imagePath)
    channelH, _, _ = convertToHSV(image)
    hist = histogram(channelH)
    binary = binaryImage(hist, channelH)
    morph = morphologicOperation(binary)


def readImage(imagePath):
    image = cv.imread(imagePath)
    saveImage('original', image)
    return image


def convertToHSV(imageBGR):
    imgHSV = cv.cvtColor(imageBGR, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(imgHSV)
    saveImage('channel_h', h)
    return h, s, v


def histogram(image):
    # ambos resultam no mesmo histograma
    # mas o do matplotlib fica mais visual, por isso
    # to salvando manualmente esse
    hist = cv.calcHist([image], [0], None, [180], [0, 180])
    plt.hist(image.ravel(), 180, [0, 180])
    plt.title("histograma H")
    saveImage('hist', None, 'plt')
    return hist


def binaryImage(hist, image):
    # o que nao se encontra no range fica preto
    # o que está no range fica branco
    pathColor = findPathPosition(hist)
    binImage = cv.inRange(image, pathColor-1, pathColor+1)
    saveImage('binary', binImage)
    return binImage


def findPathPosition(hist):
    _, max, _, maxLoc = cv.minMaxLoc(hist)
    maxValue = np.where(hist == maxLoc)[0]
    # fazer algum tratamento para encontrar
    # qual dos max locais que representam o caminho
    # por enquanto retorna manual

    # criar uma funcao que retorna um array de tuplas
    # a funcao recebe como parametro o histograma e o range
    # para encontrar os max locais, ela verifica se os
    # valores anteriores e posterioes sao menores e se for
    # adciona aquele valor como um maximo local
    # para o array [0,2,4,6,4,2,1,5,1,2] deve
    # retornar um array [(3,6), (7,5)]

    # alterar o valor retornado
    return 33


def morphologicOperation(image):

    strElement = cv.getStructuringElement(cv.MORPH_RECT, (8, 8))
    morph = cv.morphologyEx(image, cv.MORPH_ERODE, strElement)

    for i in range(8):
        strElement = cv.getStructuringElement(cv.MORPH_ELLIPSE, (15, 15))
        morph = cv.morphologyEx(morph, cv.MORPH_DILATE, strElement)

    for i in range(4):
        strElement = cv.getStructuringElement(cv.MORPH_ELLIPSE, (17, 17))
        morph = cv.morphologyEx(morph, cv.MORPH_ERODE, strElement)

    saveImage('morphologic', morph)
    return morph


def saveImage(name, image, provider='cv'):
    prefix = './images/pre_processing/'
    sufix = '.png'
    path = prefix + name + sufix

    if provider == 'cv':
        cv.imwrite(path, image)
    elif provider == 'plt':
        plt.savefig(path)


def getImage(name):
    prefix = './images/maps/'
    sufix = '.png'
    return prefix + name + sufix


main()
