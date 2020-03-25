import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import QFile, Qt, Signal, QThread
from PySide2.QtGui import QPixmap
from MainWindow_ui import Ui_MainWindow
from Manager import Manager


class MainWindow(QMainWindow):
    startBut = Signal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.manager = Manager(self)
        self.__threadRun = QThread()
        self.__threadRun.start()
        self.manager.moveToThread(self.__threadRun)

        self.ui.openFile_button.clicked.connect(self.openFileButtonClicked)
        self.ui.start_button.clicked.connect(self.startButtonClicked)
        self.startBut.connect(self.manager.startButtonClicked)

        self.manager.sendMessageConsole.connect(self.setMessage)

    def setMessage(self, message):
        self.ui.console_textBrowser.append(message)

    def openFileButtonClicked(self):
        path_to_file, _ = QFileDialog.getOpenFileName(self, self.tr("Load Image"), self.tr("~/Desktop/"), self.tr("Images (*.png *.jpg)"))
        self.manager.setImage(path_to_file)
        pix = QPixmap(path_to_file)
        pix = pix.scaled(640, 480, Qt.KeepAspectRatio)
        self.ui.inputImage_label.setPixmap(pix)

    def startButtonClicked(self):
        self.startBut.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
