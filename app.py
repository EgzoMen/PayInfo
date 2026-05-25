from PySide6.QtWidgets import QApplication, QMainWindow
from sources.forms.start_window import Ui_StartWindow
from sources.widgets_slot import buttons


class App(QMainWindow):
    def __init__(self):
        self._init_components()
    
    def _init_components(self):
        "Window"
        super().__init__()
        self.ui_elements = Ui_StartWindow()
        self.ui_elements.setupUi(self)
        self.show()

        "Buttons"
        self.btn_actions = buttons.ButtonAction()
        self.btn_actions.bind(self.ui_elements)
        

if __name__ == "__main__":
    app = QApplication([])
    window = App()
    app.exec()