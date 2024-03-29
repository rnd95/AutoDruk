from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QListView, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QWidget, QMessageBox)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(863, 617)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionVersion_0_1b = QAction(MainWindow)
        self.actionVersion_0_1b.setObjectName(u"actionVersion_0_1b")
        self.actionVersion_0_1b.setCheckable(True)
        self.actionVersion_0_1b.setEnabled(True)
        self.actionVersion_0_1b.setVisible(True)
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.action_4.setFont(font1)
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_6.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(0, 40, 251, 441))
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(110, 550, 64, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 863, 21))
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
        self.menu.addAction(self.action_6)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionVersion_0_1b)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AutoDruk (beta) - {applet_name}", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0438\u0442\u0438 \u0430\u043f\u043b\u0435\u0442", None))
        self.actionVersion_0_1b.setText(QCoreApplication.translate("MainWindow", u"Version 0.1b", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043c\u0456\u043d\u0438\u0442\u0438 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0456\u044e", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0445\u0456\u0434", None))
#if QT_CONFIG(statustip)
        self.action_6.setStatusTip(QCoreApplication.translate("MainWindow", u"Alt+F4", None))
#endif // QT_CONFIG(statustip)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0444\u0456\u0433\u0443\u0440\u0430\u0446\u0456\u044f", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0432\u0456\u0434\u043a\u0430", None))