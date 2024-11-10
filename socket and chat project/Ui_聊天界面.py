# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '聊天界面.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(820, 639)
        Form.setMaximumSize(QSize(820, 640))
        Form.setWindowOpacity(1.000000000000000)
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(60, 10, 700, 420))
        self.listWidget.setMaximumSize(QSize(700, 420))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 450, 541, 51))
        font = QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(620, 450, 141, 51))
        font1 = QFont()
        font1.setPointSize(13)
        self.pushButton.setFont(font1)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(60, 520, 351, 91))
        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 40, 161, 20))
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 40, 75, 23))
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(440, 520, 321, 91))
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(70, 40, 191, 20))
        self.down = QPushButton(Form)
        self.down.setObjectName(u"down")
        self.down.setGeometry(QRect(770, 400, 31, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 620, 171, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8f93\u5165\u804a\u5929\u5ba4\u53f7\u7801", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u52a0\u5165", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u4f60\u5728\u804a\u5929\u5ba4\u7684\u540d\u5b57", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u5fc5\u586b", None))
        self.down.setText(QCoreApplication.translate("Form", u"\u25bc", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u804a\u5929\u5ba4\u4eba\u6570\u4e3a\uff1a1", None))
    # retranslateUi

