import cv2 as cv
import image as img
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def heatmap():
    weightsImage = cv.imread(img.get('result_heatmap'), mode='BIN')

    max = weightsImage[300, 200]
    # min, max, minloc, maxloc = cv.minMaxLoc(weightsImage)

    print(max)


heatmap()
