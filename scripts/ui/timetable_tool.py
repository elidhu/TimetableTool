# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timetable_tool.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(438, 396)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 60, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 210, 251, 96))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.user_lbl = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_lbl.setFont(font)
        self.user_lbl.setObjectName(_fromUtf8("user_lbl"))
        self.horizontalLayout.addWidget(self.user_lbl)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pass_lbl = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass_lbl.setFont(font)
        self.pass_lbl.setObjectName(_fromUtf8("pass_lbl"))
        self.horizontalLayout_2.addWidget(self.pass_lbl)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.login_btn = QtGui.QPushButton(self.widget)
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.verticalLayout.addWidget(self.login_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.login_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.copy)
        QtCore.QObject.connect(self.login_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.copy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Timetable Tool", None))
        self.label.setText(_translate("MainWindow", "OASIS Login", None))
        self.user_lbl.setText(_translate("MainWindow", "USERNAME", None))
        self.pass_lbl.setText(_translate("MainWindow", "PASSWORD", None))
        self.login_btn.setText(_translate("MainWindow", "Login", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
