from PyQt5 import QtWidgets
from form import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.EncryptButton.clicked.connect(self.encButton_clicked)
        self.ui.DecryptButton.clicked.connect(self.decButton_clicked)

    def encButton_clicked(self):
        self.encrypt()

    def decButton_clicked(self):
        self.decrypt()

    @staticmethod
    def get_xord(gamma: str, message: list) -> list:
        for i in range(len(message)):
            message[i] = chr(ord(message[i]) ^ ord(gamma[i % len(gamma)]))
        return message

    def encrypt(self):
        gamma1 = self.ui.LineGamma1.text()
        gamma2 = self.ui.LineGamma2.text()
        gamma3 = self.ui.LineGamma3.text()
        message = self.ui.Message.toPlainText()
        if len(message) and len(gamma1) and len(gamma2) and len(gamma3):
            message = self.get_xord(gamma1, list(message))
            message = self.get_xord(gamma2, message)
            message = self.get_xord(gamma3, message)

            for i in range(len(message)):
                message[i] = str(ord(message[i]))

            text = ""
            for i in range(len(message)):
                text = text + message[i] + " "

            self.ui.Ciphergramm.setText(text)

    def decrypt(self):
        gamma1 = self.ui.LineGamma12.text()
        gamma2 = self.ui.LineGamma22.text()
        gamma3 = self.ui.LineGamma32.text()
        ciphergramm = list(map(int, self.ui.Ciphergramm2.toPlainText().split(' ')))

        if len(ciphergramm) and len(gamma1) and len(gamma2) and len(gamma3):
            ciphergramm = self.get_xord(gamma1, list(map(chr, ciphergramm)))
            ciphergramm = self.get_xord(gamma2, ciphergramm)
            ciphergramm = self.get_xord(gamma3, ciphergramm)

            text = "".join(ciphergramm)
            self.ui.Message2.setText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()

    sys.exit(app.exec())



