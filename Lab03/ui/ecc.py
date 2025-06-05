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
        self.lbl_header.setGeometry(QtCore.QRect(250, 20, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.lbl_header.setFont(font)
        self.lbl_header.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_header.setText("ECC CIPHER")

        # Generate Keys
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(580, 30, 150, 30))
        self.btn_gen_keys.setText("Generate Keys")

        # Labels
        font_label = QtGui.QFont()
        font_label.setPointSize(11)

        self.lbl_inf = QtWidgets.QLabel(self.centralwidget)
        self.lbl_inf.setGeometry(QtCore.QRect(120, 100, 100, 25))
        self.lbl_inf.setFont(font_label)
        self.lbl_inf.setText("Information")

        self.lbl_sign = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sign.setGeometry(QtCore.QRect(120, 210, 100, 25))
        self.lbl_sign.setFont(font_label)
        self.lbl_sign.setText("Signature")

        # Text Areas
        self.txt_inf = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_inf.setGeometry(QtCore.QRect(220, 90, 450, 80))

        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(220, 200, 450, 80))

        # Buttons
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(220, 300, 100, 30))
        self.btn_sign.setText("Sign")

        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(370, 300, 100, 30))
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
        MainWindow.setWindowTitle("ECC Cipher")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
