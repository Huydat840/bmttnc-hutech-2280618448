from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Header
        self.lbl_header = QtWidgets.QLabel(self.centralwidget)
        self.lbl_header.setGeometry(QtCore.QRect(250, 10, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.lbl_header.setFont(font)
        self.lbl_header.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_header.setText("RSA CIPHER")

        # Generate Keys
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(580, 20, 150, 30))
        self.btn_gen_keys.setText("Generate Keys")

        # Labels
        font_label = QtGui.QFont()
        font_label.setPointSize(11)

        self.lbl_plaintext = QtWidgets.QLabel(self.centralwidget)
        self.lbl_plaintext.setGeometry(QtCore.QRect(60, 80, 100, 25))
        self.lbl_plaintext.setFont(font_label)
        self.lbl_plaintext.setText("Plaintext")

        self.lbl_ciphertext = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ciphertext.setGeometry(QtCore.QRect(60, 180, 100, 25))
        self.lbl_ciphertext.setFont(font_label)
        self.lbl_ciphertext.setText("Ciphertext")

        self.lbl_infor = QtWidgets.QLabel(self.centralwidget)
        self.lbl_infor.setGeometry(QtCore.QRect(420, 80, 100, 25))
        self.lbl_infor.setFont(font_label)
        self.lbl_infor.setText("Information")

        self.lbl_sign = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sign.setGeometry(QtCore.QRect(420, 180, 100, 25))
        self.lbl_sign.setFont(font_label)
        self.lbl_sign.setText("Signature")

        # TextEdits
        self.txt_plain = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain.setGeometry(QtCore.QRect(150, 70, 240, 80))

        self.txt_cipher = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher.setGeometry(QtCore.QRect(150, 170, 240, 80))

        self.txt_inf = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_inf.setGeometry(QtCore.QRect(510, 70, 240, 80))

        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(510, 170, 240, 80))

        # Buttons
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(150, 270, 100, 30))
        self.btn_encrypt.setText("Encrypt")

        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(290, 270, 100, 30))
        self.btn_decrypt.setText("Decrypt")

        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(510, 270, 100, 30))
        self.btn_sign.setText("Sign")

        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(650, 270, 100, 30))
        self.btn_verify.setText("Verify")

        # Final setup
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("RSA Cipher")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
