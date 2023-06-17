import matplotlib.pyplot as plt
import preprocessing
import image as img
import cv2 as cv
import numpy as np
import time
import matplotlib as mpl


# select_roi
# https://www.dobitaobyte.com.br/capturar-regiao-de-interesse-com-opencv/
# https://www.educba.com/opencv-bounding-box/

def colorFader(hot, medium, cold, mix=0):
    if(mix > 0.5):  # fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
        return ((2-(2*mix))*medium + ((2*mix)-1)*hot)
    return ((1-(2*mix))*cold + 2*mix*medium)


def main():
    red = np.array([0.0, 0.0, 255.0])
    green = np.array([0.0, 255.0, 0.0])
    blue = np.array([255.0, 0.0, 0.0])

    binary = preprocessing.main()

    height = len(binary)
    width = len(binary[0])

    weightsResult = np.zeros((height, width), dtype=np.float64)

    i = 0
    until = width*height

    # substituir bitwise por roi
    # https: // answers.opencv.org/question/101116/pixel-datas-in-a-circular-region/^
    # https: // stackoverflow.com/questions/25668828/how-to-create-colour-gradient-in-python
    # verde pra vermelho

    startTime = time.time()
    for w0 in range(width):
        for h0 in range(height):
            if binary[h0, w0] != 255:
                andImage = cv.bitwise_and(cv.inRange(cv.circle(np.zeros(
                    (height, width), dtype=np.int32), (w0, h0), 300, 255, -1), 240, 255), binary)
                data = np.asarray(andImage, dtype=np.int64)
                weightsResult[h0, w0] = data.sum()

            i = i+1
            print("--- {:02f}%: {} de {} --- data: {} ---".format((i *
                                                                   100)/until, i, until, weightsResult[h0, w0]))

    try:
        img.save('weightsResult', weightsResult)
    except:
        print("f")

    print(time.time() - startTime)

    maxVal = weightsResult.max()
    print(maxVal)
    cv.waitKey(1000)

    percentualResult = np.zeros((height, width), dtype=np.float16)
    i = 0
    for w1 in range(width):
        for h1 in range(height):
            percentualResult[h1, w1] = weightsResult[h1, w1]/maxVal
            i = i+1
            print("--- {:02f}%: {} de {} --- percentual: {:02f} ---".format(
                (i*100)/until, i, until,  percentualResult[h1, w1]))

    i = 0
    heatmap = np.zeros((height, width, 3), dtype="uint8")
    for w2 in range(width):
        for h2 in range(height):
            heatmap[h2, w2] = colorFader(
                red, green, blue, percentualResult[h2, w2]
            )
            i = i+1
            print("--- {:02f}%: {} de {} --- color: {} ---".format(
                (i*100)/until, i, until,  heatmap[h2, w2]))

    try:
        img.save('trueHeatmap_2', heatmap)
    except:
        print('f')

    morphologic = cv.imread(img.get('morphologic'))
    result = cv.imread(img.get('trueHeatmap_2'))

    fig = plt.figure(figsize=(15, 7))

    morphologic_not = cv.bitwise_not(morphologic)

    resultMap = cv.bitwise_and(morphologic_not, result)

    img.save('heatmap_and_path_2', resultMap)

    fig = plt.figure(figsize=(15, 7))

    ax1 = fig.add_subplot(121)
    plt.imshow(resultMap)

    ax2 = fig.add_subplot(122)
    plt.imshow(result)

    plt.show()

    fig = plt.figure(figsize=(15, 7))

    # ax1 = fig.add_subplot(121)
    # plt.imshow(heatmap)

    # ax2 = fig.add_subplot(122)
    # plt.imshow(percentualResult)

    # plt.show()

    # plt.imshow(heatmap)


main()
