from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys
from Six_Number import Ui_MainWindow

# Creat app
app = QtWidgets.QApplication(sys.argv)

# init
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


# Logic
def add_function():
    list = [i for i in range(1, 50)]
    result = random.choices(list, k=6)
    out_print = str(result).strip("[]")
    ui.label.setText(out_print)


# Обработка нажатия кнопки
ui.btn_1.clicked.connect(add_function)

# Main Loop
sys.exit(app.exec_())
