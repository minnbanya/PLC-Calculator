import sys, os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLCDNumber

from components.lexicalAnalyzer import MyLexer
from components.syntexAnalyzer import MyParser
# from components.memory import Memory

class MainWindow(QMainWindow):

    # Do this for intellisense
    button_1:QPushButton
    button_2:QPushButton
    button_3:QPushButton
    button_4:QPushButton
    button_5:QPushButton
    button_6:QPushButton
    button_7:QPushButton
    button_8:QPushButton
    button_9:QPushButton
    button_0:QPushButton
    button_delete:QPushButton
    button_ce:QPushButton
    button_plus:QPushButton
    button_star:QPushButton
    button_equal:QPushButton
    input_text:QLineEdit
    output_lcd:QLCDNumber
    prefix_lcd:QLineEdit
    postfix_lcd:QLineEdit
    error_display:QLineEdit

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("main.ui", self)

        #### Binding button to function ####
        # Methods:
        self.button_1.clicked.connect(lambda: self.push("1"))
        self.button_2.clicked.connect(lambda: self.push("2"))
        self.button_3.clicked.connect(lambda: self.push("3"))
        self.button_4.clicked.connect(lambda: self.push("4"))
        self.button_5.clicked.connect(lambda: self.push("5"))
        self.button_6.clicked.connect(lambda: self.push("6"))
        self.button_7.clicked.connect(lambda: self.push("7"))
        self.button_8.clicked.connect(lambda: self.push("8"))
        self.button_9.clicked.connect(lambda: self.push("9"))
        self.button_0.clicked.connect(lambda: self.push("0"))

        self.button_delete.clicked.connect(self.push_delete)
        self.button_ce.clicked.connect(self.push_ce)

        self.button_plus.clicked.connect(lambda: self.push("+"))
        self.button_star.clicked.connect(lambda: self.push("*"))

        self.button_equal.clicked.connect(self.push_equal)
        self.input_text.returnPressed.connect(self.push_equal)

    # def push_1(self):
    #     current_text:str = self.input_text.text()
    #     self.input_text.setText(f"{current_text}1")
    
    def push(self, text:str):
        current_text:str = self.input_text.text()
        self.input_text.setText(f"{current_text}{text}")

    def push_delete(self):
        current_text:str = self.input_text.text()
        current_text = current_text[:-1]
        self.input_text.setText(current_text)
    
    def push_ce(self):
        self.input_text.clear()
    
    def push_equal(self):
        print("Calculate")
        lexer = MyLexer()
        parser = MyParser()
        # memory = Memory()
        input_text = self.input_text.text()
        results = parser.parse(lexer.tokenize(input_text))
        if results is None:
            self.output_lcd.display(0)
            self.prefix_lcd.clear()
            self.postfix_lcd.clear()
            self.error_display.setText('Invalid Input')
        else:
            self.error_display.clear()
            result = results[0]
            prefix = results[1]
            postfix = results[2]
            print(type(result))
            print(f"Prefix: {prefix}")
            print(f"Postfix: {postfix}")
            self.output_lcd.display(result)
            self.prefix_lcd.setText(prefix)
            self.postfix_lcd.setText(postfix)
        # for debug
        # print(memory)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()