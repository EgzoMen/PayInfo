# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        if not StartWindow.objectName():
            StartWindow.setObjectName(u"StartWindow")
        StartWindow.resize(746, 637)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 321, 601))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.product_table = QTableWidget(self.layoutWidget)
        if (self.product_table.columnCount() < 2):
            self.product_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.product_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.product_table.rowCount() < 1):
            self.product_table.setRowCount(1)
        self.product_table.setObjectName(u"product_table")
        self.product_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.product_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.product_table.setRowCount(1)
        self.product_table.horizontalHeader().setVisible(True)
        self.product_table.horizontalHeader().setCascadingSectionResizes(False)
        self.product_table.horizontalHeader().setDefaultSectionSize(160)
        self.product_table.horizontalHeader().setHighlightSections(True)
        self.product_table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.product_table)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_row_btn = QPushButton(self.layoutWidget)
        self.add_row_btn.setObjectName(u"add_row_btn")

        self.horizontalLayout.addWidget(self.add_row_btn)

        self.remove_row_btn = QPushButton(self.layoutWidget)
        self.remove_row_btn.setObjectName(u"remove_row_btn")

        self.horizontalLayout.addWidget(self.remove_row_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(380, 20, 345, 273))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.calendar = QCalendarWidget(self.layoutWidget1)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.calendar.setGridVisible(True)
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(True)

        self.verticalLayout_2.addWidget(self.calendar)

        self.save_record_btn = QPushButton(self.layoutWidget1)
        self.save_record_btn.setObjectName(u"save_record_btn")

        self.verticalLayout_2.addWidget(self.save_record_btn)

        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)

        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle(QCoreApplication.translate("StartWindow", u"\u041f\u043e\u0434\u0441\u0447\u0451\u0442 \u0437\u0430\u0442\u0440\u0430\u0442", None))
        ___qtablewidgetitem = self.product_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StartWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        ___qtablewidgetitem1 = self.product_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StartWindow", u"\u0417\u0430\u0442\u0440\u0430\u0447\u0435\u043d\u043e", None))
        self.add_row_btn.setText(QCoreApplication.translate("StartWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.remove_row_btn.setText(QCoreApplication.translate("StartWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.save_record_btn.setText(QCoreApplication.translate("StartWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
    # retranslateUi

