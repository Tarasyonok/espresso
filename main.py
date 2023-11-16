import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.show_info()

    def show_info(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM info""").fetchall()

        title = ["ID", "название сорта", "степень обжарки", "молотый/в зернах", "описание вкуса", "цена",
                 "объем упаковки"]
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Coffee()
    w.show()
    sys.exit(app.exec())
