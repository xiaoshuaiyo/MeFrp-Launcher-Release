import sys

from PyQt5.QtCore import Qt, QEventLoop, QTimer, QSize
from PyQt5.QtCore import Qt, pyqtSignal, QSize
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QColor
from PyQt5.QtWidgets import QApplication, QWidget

from qfluentwidgets import SplitFluentWindow, FluentIcon

from uiaif import Form
from uibif import Form2
from uicif import Form3
from qfluentwidgets import (NavigationInterface,NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, setThemeColor)

class window(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.resize(850, 500)
        # 居中
        rect = QApplication.desktop().availableGeometry(
        )
        w, h = rect.width(), rect.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.windowEffect.setMicaEffect(self.winId())
        setTheme(Theme.AUTO)

        # 更改主题色
        setThemeColor("#28afe9")


        self.setQss()

        self.setWindowTitle("MeFrp")




        # 添加子界面
        self.form = Form(self)
        self.form2 = Form2(self)
        self.form3 = Form3(self)


        self.addSubInterface(self.form, FluentIcon.HOME, '简单启动')
        self.addSubInterface(self.form2, FluentIcon.ALIGNMENT, '高级启动')

        # 添加关于按钮
        self.addSubInterface(self.form3, icon=FluentIcon.INFO, text="关于", position=NavigationItemPosition.BOTTOM)



    def createSubInterface(self):
        loop = QEventLoop(self)
        QTimer.singleShot(3000, loop.quit)
        loop.exec()

    def setQss(self):
        color = 'dark' if isDarkTheme() else 'light'
        with open(f'resource/{color}/demo.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())



if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = window()
    w.show()
    app.exec_()