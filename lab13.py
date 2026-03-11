#Oskar Górczyñski, 57785, 3/3
import PyQt5.QtWidgets as QtWidgets
from PyQt5 import QtCore
# Zadanie 1
app=QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setWindowTitle("Zadanie 1")
etykieta= QtWidgets.QLabel("")
przycisk=QtWidgets.QPushButton("Kliknij mnie")
przycisk.clicked.connect(lambda: etykieta.setText("Pierwszy program gotowy!"))
uklad=QtWidgets.QVBoxLayout()
uklad.addWidget(etykieta)
uklad.addWidget(przycisk)
window.setLayout(uklad)
window.show()
app.exec_()
# Zadanie 2
kalkulator=QtWidgets.QApplication([])
okno=QtWidgets.QWidget()
okno.setWindowTitle("Kalkulator")
wyswietlacz=QtWidgets.QLineEdit("")
wyswietlacz.setReadOnly(True)
wyswietlacz.setAlignment(QtCore.Qt.AlignRight)
wyswietlacz.setStyleSheet("font-size: 20px;")

# Buttons
buttons = {
    "0": QtWidgets.QPushButton("0"),
    "1": QtWidgets.QPushButton("1"),
    "2": QtWidgets.QPushButton("2"),
    "3": QtWidgets.QPushButton("3"),
    "4": QtWidgets.QPushButton("4"),
    "5": QtWidgets.QPushButton("5"),
    "6": QtWidgets.QPushButton("6"),
    "7": QtWidgets.QPushButton("7"),
    "8": QtWidgets.QPushButton("8"),
    "9": QtWidgets.QPushButton("9"),
    "+": QtWidgets.QPushButton("+"),
    "-": QtWidgets.QPushButton("-"),
    "*": QtWidgets.QPushButton("*"),
    "/": QtWidgets.QPushButton("/"),
    "=": QtWidgets.QPushButton("="),
    "C": QtWidgets.QPushButton("C"),
    "DEL": QtWidgets.QPushButton("DEL"),
    ".": QtWidgets.QPushButton(".")
}

current_value = ""
operation = None
result = None

def handle_number_click(number):
    global current_value
    if number == ".":
        if "." not in current_value:
            current_value += number
    else:
        current_value += number
    wyswietlacz.setText(current_value)

def handle_operation(op):
    global current_value, operation, result
    if current_value:
        result = float(current_value)
        current_value = ""
        operation = op
        wyswietlacz.setText(f"{result} {operation}")

def handle_equals():
    global current_value, operation, result
    if current_value and operation:
        try:
            if operation == "+":
                result += float(current_value)
            elif operation == "-":
                result -= float(current_value)
            elif operation == "*":
                result *= float(current_value)
            elif operation == "/":
                result /= float(current_value)
            wyswietlacz.setText(str(result))
            current_value = str(result)
            operation = None
        except ZeroDivisionError:
            wyswietlacz.setText("Error: Division by zero")
            current_value = ""
            operation = None

def handle_clear():
    global current_value, operation, result
    current_value = ""
    operation = None
    result = None
    wyswietlacz.setText("")

def handle_delete():
    global current_value
    if current_value:
        current_value = current_value[:-1]
        wyswietlacz.setText(current_value)

for key, button in buttons.items():
    if key.isdigit() or key == ".":
        button.clicked.connect(lambda _, k=key: handle_number_click(k))
    elif key in "+-*/":
        button.clicked.connect(lambda _, k=key: handle_operation(k))
    elif key == "=":
        button.clicked.connect(handle_equals)
    elif key == "C":
        button.clicked.connect(handle_clear)
    elif key == "DEL":
        button.clicked.connect(handle_delete)

layout = QtWidgets.QVBoxLayout()
layout.addWidget(wyswietlacz)
grid = QtWidgets.QGridLayout()
positions = [(i, j) for i in range(5) for j in range(4)]
keys = ["7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        ".", "0", "=", "+",
        "DEL","C"]
for pos, key in zip(positions, keys):
    grid.addWidget(buttons[key], *pos)
layout.addLayout(grid)
okno.setLayout(layout)
okno.show()
kalkulator.exec_()

# Zadanie 3
class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.layout= QtWidgets.QVBoxLayout()
        self.label=QtWidgets.QLabel("Podaj liczbe: ")
        self.firsttext=QtWidgets.QLineEdit("")
        self.secondtext=QtWidgets.QLineEdit("")
        self.acceptbtn=QtWidgets.QPushButton("Akceptuj")
        self.acceptbtn.clicked.connect(self.accept)
        self.denybtn=QtWidgets.QPushButton("Odrzuc")
        self.denybtn.clicked.connect(self.reject)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.firsttext)
        self.layout.addWidget(self.secondtext)
        self.layout.addWidget(self.acceptbtn)
        self.layout.addWidget(self.denybtn)
        self.setLayout(self.layout)

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300,300)
        self.layout = QtWidgets.QVBoxLayout()
        self.wynik= QtWidgets.QLabel("")
        self.button = QtWidgets.QPushButton("Pokaz okno dialogowe")
        self.button.clicked.connect(self.on_show_dialog)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.wynik)
        self.setLayout(self.layout)
        self.show()

    def on_show_dialog(self):
        dial = Dialog()
        if dial.exec_() == QtWidgets.QDialog.Accepted:
            liczba1 = float(dial.firsttext.text())
            liczba2 = float(dial.secondtext.text())
            self.wynik.setText(f"Wynik: {liczba1} + {liczba2} = {liczba1+liczba2}")
        else:
            self.wynik.setText("Dialog zostal odrzucony")

app3 = QtWidgets.QApplication([])
okno3= MainWindow()
app3.exec()
