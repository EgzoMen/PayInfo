from PySide6.QtWidgets import QMessageBox


class Message:
    @classmethod
    def show_invalid_value_message(cls, line_number):
        cls.message = QMessageBox()
        cls.message.setWindowTitle('Input error')
        cls.message.setText(f'Invalid input at {line_number} line')
        cls.message.show()