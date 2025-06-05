from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '../platforms'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Tiêu đề
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 20, 500, 60))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # Label PlainText
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 120, 30))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # PlainText
        self.txtPlaintext = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPlaintext.setGeometry(QtCore.QRect(160, 100, 900, 100))
        self.txtPlaintext.setObjectName("txtPlaintext")

        # Label Key
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 220, 120, 30))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # Key
        self.txtKey = QtWidgets.QTextEdit(self.centralwidget)
        self.txtKey.setGeometry(QtCore.QRect(160, 220, 300, 40))
        self.txtKey.setObjectName("txtKey")

        # Label CipherText
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 280, 120, 30))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # CipherText
        self.txtCipherText = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCipherText.setGeometry(QtCore.QRect(160, 280, 900, 150))
        self.txtCipherText.setObjectName("txtCipherText")

        # Encrypt Button
        self.btEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btEncrypt.setGeometry(QtCore.QRect(350, 460, 150, 40))
        font.setPointSize(10)
        self.btEncrypt.setFont(font)
        self.btEncrypt.setObjectName("btEncrypt")

        # Decrypt Button
        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt.setGeometry(QtCore.QRect(600, 460, 150, 40))
        font.setPointSize(10)
        self.btnDecrypt.setFont(font)
        self.btnDecrypt.setObjectName("btnDecrypt")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caesar Cipher"))
        self.label.setText(_translate("MainWindow", "CAESAR CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plain Text:"))
        self.label_3.setText(_translate("MainWindow", "Key:"))
        self.label_4.setText(_translate("MainWindow", "CipherText:"))
        self.btEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btnDecrypt.setText(_translate("MainWindow", "Decrypt"))
