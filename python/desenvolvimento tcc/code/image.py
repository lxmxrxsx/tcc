import cv2 as cv
from matplotlib import pyplot as plt


def save(name, image, provider='cv'):
    prefix = './images/pre_processing/'
    sufix = '.png'
    path = prefix + name + sufix

    if provider == 'cv':
        cv.imwrite(path, image)
    elif provider == 'plt':
        plt.savefig(path)


def get(name):
    prefix = './images/maps/'
    sufix = '.png'
    return prefix + name + sufix
