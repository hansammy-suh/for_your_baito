import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("how much is this month's salary?")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())
