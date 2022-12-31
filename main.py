from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QTextEdit, QLineEdit
from PyQt5 import uic
from FaceBook_Class import FaceBookBot


class BotApp(QMainWindow):
    def __init__(self):
        super(BotApp, self).__init__()
        uic.loadUi("pyqt5/facebook.ui", self)
        # interface:
        self.head = self.findChild(QLabel, "header")
        self.image = self.findChild(QLabel, "image")
        self.email = self.findChild(QLineEdit, "email")
        self.password = self.findChild(QLineEdit, "password")
        self.first = self.findChild(QLineEdit, "first")
        self.third = self.findChild(QLineEdit, "third")
        self.start_button = self.findChild(QPushButton, "start")
        self.answer = self.findChild(QLabel, "answer")

        # Action:
        self.start_button.clicked.connect(self.launch_bot)

        self.show()

    # ========================= FUNCTIONALITY ======================== #
    def launch_bot(self):
        email = self.email.text()
        password = self.password.text()
        first_group = self.first.text()
        my_number = self.third.text()
        # bot section:
        my_bot = FaceBookBot()
        my_bot.login_facebook(my_email=email, my_password=password)
        my_bot.find_group(group_name=first_group)
        my_bot.join_group(quantity=my_number)
        self.answer.setStyleSheet("background-color: rgb(144, 238, 144); border: 2px solid rgb(0, 100, 0); "
                                  "color: rgb(0, 0, 128); border-radius: 10px;")
        self.answer.setText("Operation Has Completed!")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    facebook = BotApp()
    sys.exit(app.exec_())
