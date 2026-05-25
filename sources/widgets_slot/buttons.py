from ..forms.start_window import Ui_StartWindow


class ButtonAction:
    def bind(self, ui_elements: Ui_StartWindow):
        self.ui_elements = ui_elements

        self.ui_elements.add_row_btn.clicked.connect(self.add_row)
        self.ui_elements.remove_row_btn.clicked.connect(self.remove_row)

    def add_row(self):
        row_count = self.ui_elements.product_table.rowCount()
        self.ui_elements.product_table.insertRow(row_count)

    def remove_row(self):
        row_count = self.ui_elements.product_table.rowCount()
        self.ui_elements.product_table.removeRow(row_count - 1)
        