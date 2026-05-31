from ..forms.start_window import Ui_StartWindow
from ..db import *


class ButtonAction:
    def __init__(self, ui_elements: Ui_StartWindow):
        self.ui_elements = ui_elements

        self.ui_elements.add_row_btn.clicked.connect(self.add_row)
        self.ui_elements.remove_row_btn.clicked.connect(self.remove_row)
        self.ui_elements.save_record_btn.clicked.connect(self.save_product)

    def add_row(self):
        row_count = self.ui_elements.product_table.rowCount()
        self.ui_elements.product_table.insertRow(row_count)

    def remove_row(self):
        row_count = self.ui_elements.product_table.rowCount()
        self.ui_elements.product_table.removeRow(row_count - 1)
        
    def save_product(self):
        chossen_date = self.ui_elements.calendar.selectedDate().toString('dd-MM-yyyy')

        products = {}
        for i in range(self.ui_elements.product_table.rowCount()):
            name = self.ui_elements.product_table.item(i, 0).text()
            spent = self.ui_elements.product_table.item(i, 1).text()
            
            products.update({name: float(spent)})
        
        product_collection.update_one(
            {'date': chossen_date},
            {
                '$set': {
                    'products': products,
                    'total_cost': sum(products.values())
                }
            },
            upsert=True
        )
        print(products)

