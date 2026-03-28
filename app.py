from sources.start_window import Ui_StartWindow
from PySide6.QtWidgets import QApplication, QMainWindow


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_components = Ui_StartWindow()
        self.ui_components.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    app.exec()