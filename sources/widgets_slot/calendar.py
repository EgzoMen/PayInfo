from PySide6.QtWidgets import QTableWidgetItem
from ..forms.start_window import Ui_StartWindow
from ..db import *


class CalendarAction:
    def __init__(self, ui_elements: Ui_StartWindow):
        self.ui_elements = ui_elements
        
        self.ui_elements.calendar.clicked.connect(self.show_data_by_date)

    def show_data_by_date(self):
        chossen_date = self.ui_elements.calendar.selectedDate().toString('dd-MM-yyyy')
        record: dict | None = product_collection.find_one({'date': f'{chossen_date}'})

        if not record:
            return
        
        products: dict = record.get('products')
        self.ui_elements.product_table.setRowCount(len(products))

        i = 0
        for name, spent in products.items():
            self.ui_elements.product_table.setItem(i, 0, QTableWidgetItem(name))  
            self.ui_elements.product_table.setItem(i, 1, QTableWidgetItem(f'{spent}'))
            i += 1 
