from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from qframelesswindow import FramelessWindow, StandardTitleBar, AcrylicWindow, TitleBar
from uia import Ui_pa


class Form(QWidget, Ui_pa):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)