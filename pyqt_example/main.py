import sys
from form import Ui_Form
from PyQt5 import QtWidgets
import cv2
from PySide2.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QPixmap, QImage


class main_program(object):
    def __init__(self, ui):
        self.ui = ui
    def open_img(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName()
        if file_name:
            image = cv2.imread(file_name)
            if image is not None:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                height, width, channel = image.shape
                bytesPerLine = 3 * width
                qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qImg)
                self.ui.label.setPixmap(pixmap.scaled(self.ui.label.size()))
            else:
                self.ui.label.setText("Error loading image")

    def set_signal(self):
        ui.pushButton.clicked.connect(self.open_img)


if __name__ == "__main__":
    app = QApplication([])
    widget = QtWidgets.QWidget()
    widget.setWindowIcon(QIcon("assets/logo.png"))
    ui = Ui_Form()
    ui.setupUi(widget)
    m = main_program(ui)
    m.set_signal()
    widget.show()
    sys.exit(app.exec_())