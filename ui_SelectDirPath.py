# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_SelectDirPath.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(415, 103)
        self.WorkDirFolder = QLineEdit(Dialog)
        self.WorkDirFolder.setObjectName(u"WorkDirFolder")
        self.WorkDirFolder.setGeometry(QRect(20, 40, 291, 21))
        self.WorkDirFolder.setAutoFillBackground(False)
        self.WorkDirFolder.setStyleSheet(u"")
        self.WorkDirFolder.setFrame(True)
        self.WorkDirFolder.setEchoMode(QLineEdit.Normal)
        self.WorkDirFolder.setReadOnly(True)
        self.WorkDirFolder.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.WorkDirFolder.setClearButtonEnabled(False)
        self.label_welcome = QLabel(Dialog)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setGeometry(QRect(20, 20, 151, 16))
        self.OK = QPushButton(Dialog)
        self.OK.setObjectName(u"OK")
        self.OK.setGeometry(QRect(330, 10, 75, 23))
        self.OpenFldWindow = QPushButton(Dialog)
        self.OpenFldWindow.setObjectName(u"OpenFldWindow")
        self.OpenFldWindow.setGeometry(QRect(330, 40, 75, 23))
        self.OpenFldWindow.setMouseTracking(False)
        self.OpenFldWindow.setCheckable(True)
        self.Exit = QPushButton(Dialog)
        self.Exit.setObjectName(u"Exit")
        self.Exit.setGeometry(QRect(330, 70, 75, 23))

        self.retranslateUi(Dialog)
        self.Exit.pressed.connect(self.Exit.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"AutoDruk - Work Directory Folder", None))
        self.WorkDirFolder.setInputMask("")
        self.WorkDirFolder.setText("")
        self.label_welcome.setText(QCoreApplication.translate("Dialog", u"\u0412\u043a\u0430\u0436\u0456\u0442\u044c \u0440\u043e\u0431\u043e\u0447\u0443 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u044e:", None))
        self.OK.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.OpenFldWindow.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.Exit.setText(QCoreApplication.translate("Dialog", u"Quit", None))
    # retranslateUi

