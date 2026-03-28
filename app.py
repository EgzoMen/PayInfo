from sources.start_window import Ui_StartWindow
from PySide6.QtWidgets import QApplication, QMainWindow


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_components = Ui_StartWindow()
        self.ui_components.setupUi(self)
        self.show()

        self.ui_components.add_row_btn.clicked.connect(self.add_row)
        self.ui_components.remove_row_btn.clicked.connect(self.remove_row)
    
    def add_row(self):
        row_count = self.ui_components.product_table.rowCount()
        self.ui_components.product_table.insertRow(row_count)

    def remove_row(self):
        row_count = self.ui_components.product_table.rowCount()
        self.ui_components.product_table.removeRow(row_count - 1)


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    app.exec()