from ..forms.start_window import Ui_StartWindow
from ..db import *
from .message_boxes import Message


class ButtonAction:
    def __init__(self, ui_elements: Ui_StartWindow):
        self.ui_elements = ui_elements

    def add_row(self):
        row_count = self.ui_elements.product_table.rowCount()
        self.ui_elements.product_table.insertRow(row_count)

    def remove_row(self):
        row_count = self.ui_elements.product_table.rowCount()
        self.ui_elements.product_table.removeRow(row_count - 1)
        
    def save_product(self):
        products = {}
        for i in range(self.ui_elements.product_table.rowCount()):
            try:
                name = self.ui_elements.product_table.item(i, 0).text()
                spent = self.ui_elements.product_table.item(i, 1).text()

                products.update({ name: float(spent) })
            except (AttributeError, ValueError):
                Message.show_invalid_value_message(i)
                return
            
        product_collection.update_one(
            {
                'date': self.ui_elements.calendar.selectedDate().toString('dd-MM-yyyy')
            },
            {
                '$set': {
                    'products': products,
                    'total_cost': sum(products.values())
                }
            },
            upsert=True
        )

    def show_mounth_spent(self):
        mounth =  self.ui_elements.calendar.selectedDate().toString('MM')

        mounth_records = product_collection.find({
          'date'  : {"$regex": rf"^[0-9]{{2}}-{mounth}-[0-9]{{4}}$"}
        })
        
        s = 0
        for record in mounth_records:
            s += record.get('total_cost', 0)
        
        self.ui_elements.label.setText(f'Spent money: {round(s, 2)}')

    def bind_events(self):
        self.ui_elements.add_row_btn.clicked.connect(self.add_row)
        self.ui_elements.remove_row_btn.clicked.connect(self.remove_row)
        self.ui_elements.save_record_btn.clicked.connect(self.save_product)
        self.ui_elements.show_mounth_spent_btn.clicked.connect(self.show_mounth_spent)
