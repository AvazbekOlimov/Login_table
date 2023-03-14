from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen
from login import Ui_Signin
class LoginUI(QMainWindow, Ui_Signin):
    def __init__(self):
        super(LoginUI, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.close_button.clicked.connect(self.close)
        self.minimize_button.clicked.connect(self.minimize)
    def close(self):
        return super().close()
    def minimize(self):
        self.showMinimized()

        
app = QApplication([])
w = LoginUI()
w.show()
app.exec()