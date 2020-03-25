from PIL import ImageDraw, ImageQt
import numpy as np
import matplotlib.pyplot as plt
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import Qt


class Processing():
    @staticmethod
    def histogram(pixels):
        import time
        start_time = time.time()
        hist = {}
        for i in range(256):
            hist[i] = 0
        for j in pixels:
            for i in j:
                hist[i] = hist[i] + 1
        print(time.time() - start_time)
        return hist

    @staticmethod
    def showHistogram(hist, name=None):
        plt.bar(range(len(hist)), list(hist.values()), align='center')
        plt.xticks(range(len(hist)), list(hist.keys()))
        if name:
            plt.savefig(name)
            return
        plt.show()

    @staticmethod
    def cdf(hist, x):
        toRet = 0
        for i in range(x+1):
            toRet += hist[i]
        return toRet

    @staticmethod
    def histogramAlignment(pixels, hist):
        import time
        start_time = time.time()
        size = len(pixels) * len(pixels[0])
        for j in range(len(pixels)):
            for i in range(len(pixels[j])):
                pixels[j][i] = np.round((Processing.cdf(hist, pixels[j][i]) - 1) * 255 / (size - 1))
        print(time.time() - start_time)
        return pixels

    @staticmethod
    def histogramApply(image, pixels):
        import time
        start_time = time.time()
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        for x in range(width):
            for y in range(height):
                temp = int(pixels[y][x])
                draw.point((x, y), temp)
        print(time.time() - start_time)
        return image

    @staticmethod
    def convertToQtFormat(frame):
        if frame is None:
            return
        rgbImage = ImageQt.ImageQt(frame)
        pix = QPixmap.fromImage(rgbImage)
        pix = pix.scaled(640, 480, Qt.KeepAspectRatio)
        return pix

    @staticmethod
    def normalizedHistogram(pixels):
        hist = {}
        size = len(pixels) * len(pixels[0])
        for i in range(256):
            hist[i] = 0

        for j in pixels:
            for i in j:
                hist[i] = hist[i] + 1
        # Processing.showHistogram(hist)

        for i in hist:
            hist[i] /= size
        Processing.showHistogram(hist)
        return hist

    @staticmethod
    def equalization(hist, normalizedHist, zm=255):
        # zm = 255
        newHist = {}
        for i in range(256):
            newHist[i] = 0

        for i in hist:
            summ = 0
            for k in range(i):
                summ += normalizedHist[k]
            newHist[i] = zm * summ
        Processing.showHistogram(newHist)
        return newHist

    @staticmethod
    def kym(hist, size):
        normHist = {}
        toRet = {}
        for i in range(256):
            normHist[i] = 0
            toRet[i] = 0

        for i in hist:
            normHist[i] = hist[i] / size

        for i in range(256):
            summ = 0
            for k in range(i):
                summ += normHist[k]
            toRet[i] = summ * 25
        Processing.showHistogram(toRet)
