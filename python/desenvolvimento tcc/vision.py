import cv2 as cv
import numpy as np


class Vision:

    # properties
    needleImage = None
    needleWidth = 0
    needleHight = 0
    method = None

    # constructor
    def __init__(self, needlePath, method=cv.TM_CCOEFF_NORMED):
        # load the image we're trying to match
        # https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
        self.needleImage = cv.imread(needlePath, cv.IMREAD_UNCHANGED)

        # Save the dimensions of the needle image
        self.needleWidth = self.needleImage.shape[1]
        self.needleHight = self.needleImage.shape[0]

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    def find(self, screen, threshold=0.5, debugMode='rectangles'):
        # run the OpenCV algorithm
        result = cv.matchTemplate(screen, self.needleImage, self.method)

        # Get the all the positions from the match result that exceed our threshold
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        # print(locations)

        # First we need to create the list of [x, y, w, h] rectangles
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]),
                    self.needleWidth, self.needleHight]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)

        # "Relative difference between sides of the rectangles to merge them into a group."
        rectangles, weights = cv.groupRectangles(
            rectangles, groupThreshold=1, eps=0.3)

        if len(rectangles):
            #print('Found needle.')

            lineColor = (0, 255, 0)
            lineType = cv.LINE_8
            markerColor = (255, 0, 255)
            markerType = cv.MARKER_CROSS

            # Loop over all the rectangles
            for (x, y, width, height) in rectangles:

                # Determine the center position
                centerX = x + int(width/2)
                centerY = y + int(height/2)

                if debugMode == 'rectangles':
                    # Determine the box position
                    topLeft = (x, y)
                    bottomRight = (x + width, y + height)
                    # Draw the box
                    cv.rectangle(screen, topLeft, bottomRight, color=lineColor,
                                 lineType=lineType, thickness=4)
                elif debugMode == 'points':
                    # Draw the center point
                    cv.drawMarker(screen, (centerX, centerY),
                                  color=markerColor, markerType=markerType,
                                  markerSize=40, thickness=2)

        if debugMode:
            return screen
