# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uic.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pc(object):
    def setupUi(self, pc):
        pc.setObjectName("pc")
        pc.resize(775, 482)
        self.TitleLabel = TitleLabel(pc)
        self.TitleLabel.setGeometry(QtCore.QRect(40, 30, 101, 38))
        self.TitleLabel.setObjectName("TitleLabel")
        self.HyperlinkButton = HyperlinkButton(pc)
        self.HyperlinkButton.setGeometry(QtCore.QRect(40, 80, 171, 51))
        self.HyperlinkButton.setObjectName("HyperlinkButton")
        self.HyperlinkButton_2 = HyperlinkButton(pc)
        self.HyperlinkButton_2.setGeometry(QtCore.QRect(400, 80, 171, 51))
        self.HyperlinkButton_2.setObjectName("HyperlinkButton_2")
        self.HyperlinkButton_3 = HyperlinkButton(pc)
        self.HyperlinkButton_3.setGeometry(QtCore.QRect(230, 80, 171, 51))
        self.HyperlinkButton_3.setObjectName("HyperlinkButton_3")
        self.StrongBodyLabel = StrongBodyLabel(pc)
        self.StrongBodyLabel.setGeometry(QtCore.QRect(50, 140, 111, 19))
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.CaptionLabel = CaptionLabel(pc)
        self.CaptionLabel.setGeometry(QtCore.QRect(50, 170, 111, 16))
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.StrongBodyLabel_2 = StrongBodyLabel(pc)
        self.StrongBodyLabel_2.setGeometry(QtCore.QRect(50, 200, 111, 19))
        self.StrongBodyLabel_2.setObjectName("StrongBodyLabel_2")
        self.CaptionLabel_2 = CaptionLabel(pc)
        self.CaptionLabel_2.setGeometry(QtCore.QRect(50, 230, 131, 16))
        self.CaptionLabel_2.setObjectName("CaptionLabel_2")
        self.StrongBodyLabel_3 = StrongBodyLabel(pc)
        self.StrongBodyLabel_3.setGeometry(QtCore.QRect(50, 260, 111, 19))
        self.StrongBodyLabel_3.setObjectName("StrongBodyLabel_3")
        self.CaptionLabel_3 = CaptionLabel(pc)
        self.CaptionLabel_3.setGeometry(QtCore.QRect(50, 290, 421, 16))
        self.CaptionLabel_3.setObjectName("CaptionLabel_3")
        self.StrongBodyLabel_4 = StrongBodyLabel(pc)
        self.StrongBodyLabel_4.setGeometry(QtCore.QRect(50, 320, 111, 19))
        self.StrongBodyLabel_4.setObjectName("StrongBodyLabel_4")
        self.CaptionLabel_4 = CaptionLabel(pc)
        self.CaptionLabel_4.setGeometry(QtCore.QRect(50, 350, 151, 61))
        self.CaptionLabel_4.setObjectName("CaptionLabel_4")

        self.retranslateUi(pc)
        QtCore.QMetaObject.connectSlotsByName(pc)

    def retranslateUi(self, pc):
        _translate = QtCore.QCoreApplication.translate
        pc.setWindowTitle(_translate("pc", "Form"))
        self.TitleLabel.setText(_translate("pc", "关于"))
        self.HyperlinkButton.setText(_translate("pc", "MeFrp Launcher\n"
"Release"))
        self.HyperlinkButton_2.setText(_translate("pc", "PyQt-Fluent-Widgets"))
        self.HyperlinkButton_3.setText(_translate("pc", "Python"))
        self.StrongBodyLabel.setText(_translate("pc", "启动器作者"))
        self.CaptionLabel.setText(_translate("pc", "小帅（xiaoshuaiyo）"))
        self.StrongBodyLabel_2.setText(_translate("pc", "版本"))
        self.CaptionLabel_2.setText(_translate("pc", "mf.launcher.Ver + 1.0.0"))
        self.StrongBodyLabel_3.setText(_translate("pc", "注明"))
        self.CaptionLabel_3.setText(_translate("pc", "本软件由MeFrp交流群内群友开发，如有侵权请立即联系我，对软件进行整改"))
        self.StrongBodyLabel_4.setText(_translate("pc", "联系我"))
        self.CaptionLabel_4.setText(_translate("pc", "<html><head/><body><p>QQ：619396351</p><p>邮箱：619396351@qq.com</p></body></html>"))
from qfluentwidgets import CaptionLabel, HyperlinkButton, StrongBodyLabel, TitleLabel
