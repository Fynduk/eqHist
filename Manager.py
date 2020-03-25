from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import QFileDialog
from Processing import Processing
from PIL import Image, ImageDraw
import numpy as np


class Manager(QObject):
    sendMessageConsole = Signal(str)

    def __init__(self, scene, parent=None):
        super().__init__(parent)
        self.__scene = scene
        self.__image = None
        self.resultImage = None

    def startButtonClicked(self):
        if self.__image is None:
            print('Wrong Image')
            return
        import time
        pixels = np.array(self.__image)
        size = len(pixels)*len(pixels[0])
        ishHist = Processing.histogram(pixels)
        Processing.showHistogram(ishHist)
        normHist = Processing.normalizedHistogram(pixels)
        trebHist = Processing.equalization(ishHist, normHist)
        Processing.kym(ishHist, size)
        Processing.kym(trebHist, size)

        self.sendMessageConsole.emit('*** Start histogram creating ***')
        start_time = time.time()
        hist = Processing.histogram(pixels)
        Processing.showHistogram(hist, 'hist')
        self.sendMessageConsole.emit('Proc time: ' + str(time.time() - start_time) + ' sec')

        self.sendMessageConsole.emit('*** Start alignment ***')
        start_time = time.time()
        pixels = Processing.histogramAlignment(pixels, hist)
        alignHist = Processing.histogram(pixels)
        Processing.showHistogram(alignHist, 'alignHist')
        self.sendMessageConsole.emit('Proc time: ' + str(time.time() - start_time) + ' sec')

        self.sendMessageConsole.emit('*** Redraw image ***')
        newNorm = Processing.normalizedHistogram(pixels)
        Processing.equalization(alignHist, newNorm, 1)
        toRet = Processing.histogramApply(self.resultImage, pixels)
        self.__scene.ui.outputImage_label.setPixmap(Processing.convertToQtFormat(toRet))
        self.saveImage(toRet)
        self.sendMessageConsole.emit('-------- Done --------')

    def setImage(self, path):
        self.__image = Image.open(path).convert('L')
        self.resultImage = Image.open(path).convert('L')

    def getImage(self):
        return self.__image

    def saveImage(self, image):
        image.save('result.png')
