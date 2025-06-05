import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        try:
            shift = int(self.ui.txt_key.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Key", "Shift key must be an integer.")
            return

        payload = {
            "text": self.ui.txt_plain_text.toPlainText(),
            "shift": shift
        }

        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data.get("encrypted", ""))
                QMessageBox.information(self, "Success", "Encrypted Successfully")
            else:
                QMessageBox.warning(self, "Error", "Encryption failed.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Connection Error", f"Error while calling API: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        try:
            shift = int(self.ui.txt_key.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Key", "Shift key must be an integer.")
            return

        payload = {
            "text": self.ui.txt_cipher_text.toPlainText(),
            "shift": shift
        }

        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data.get("decrypted", ""))
                QMessageBox.information(self, "Success", "Decrypted Successfully")
            else:
                QMessageBox.warning(self, "Error", "Decryption failed.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Connection Error", f"Error while calling API: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
