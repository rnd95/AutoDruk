# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui-Main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QListView, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(880, 570)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(88)
        sizePolicy.setVerticalStretch(57)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(True)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionVersion_0_1b = QAction(MainWindow)
        self.actionVersion_0_1b.setObjectName(u"actionVersion_0_1b")
        self.actionVersion_0_1b.setCheckable(False)
        self.actionVersion_0_1b.setEnabled(True)
        font1 = QFont()
        font1.setBold(False)
        self.actionVersion_0_1b.setFont(font1)
        self.actionVersion_0_1b.setVisible(True)
        self.actionVersion_0_1b.setMenuRole(QAction.AboutRole)
        self.actionVersion_0_1b.setIconVisibleInMenu(False)
        self.actionVersion_0_1b.setPriority(QAction.HighPriority)
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.action_4.setFont(font2)
        self.Menu_Exit = QAction(MainWindow)
        self.Menu_Exit.setObjectName(u"Menu_Exit")
        self.Menu_Exit.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 40, 251, 441))
        self.listView.setMinimumSize(QSize(251, 0))
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(300, 40, 261, 441))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(122)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setStyleSheet(u"\n"
"color: rgb(133, 229, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 880, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.Menu_Exit)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionVersion_0_1b)

        self.retranslateUi(MainWindow)
        self.Menu_Exit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AutoDruk (beta) - {applet_name}", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0438\u0442\u0438 \u0430\u043f\u043b\u0435\u0442", None))
        self.actionVersion_0_1b.setText(QCoreApplication.translate("MainWindow", u"Version 0.1b", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043c\u0456\u043d\u0438\u0442\u0438 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u044e", None))
        self.Menu_Exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0445\u0456\u0434", None))
#if QT_CONFIG(statustip)
        self.Menu_Exit.setStatusTip(QCoreApplication.translate("MainWindow", u"Alt+F4", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.listView.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0444\u0456\u0433\u0443\u0440\u0430\u0446\u0456\u044f", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0432\u0456\u0434\u043a\u0430", None))
    # retranslateUi

