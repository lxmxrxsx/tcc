import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


def colorFader(hot, medium, cold, mix=0):
    if(mix > 0.5):  # fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
        return mpl.colors.to_hex((2-(2*mix))*medium + ((2*mix)-1)*hot)
    else:
        return mpl.colors.to_hex((1-(2*mix))*cold + 2*mix*medium)


red = np.array([1.0, 0.0, 0.0])
green = np.array([0.0, 1.0, 0.0])
blue = np.array([0.0, 0.0, 1.0])
n = 500


fig, ax = plt.subplots(figsize=(8, 5))
for x in range(n+1):
    ax.axvline(x, color=colorFader(red, green, blue, x/n), linewidth=4)
plt.show()
