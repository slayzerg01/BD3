from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase
from GPPForm import GPPForm
import sys


class mainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        uic.loadUi("./ui/mainWindow.ui", self)
        self.db_init()
        self.pushButtonGPP.clicked.connect(self.GPP)

    def GPP(self):
        self.GPP = GPPForm()
        self.GPP.show()

    def db_init(self):
        self.db = QSqlDatabase().addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        self.db.setDatabaseName("gpp")
        self.db.setUserName("root")
        self.db.setPassword("qwerty123")
        if not self.db.open():
            QMessageBox.critical(self, "Ошибка!", "Соединение с БД не установлено", QMessageBox.Ok)
            print(self.db.lastError().text())

        print(self.db.isOpen())
        print(self.db.driverName())
        print(self.db.tables())
        print(self.db.databaseName())


def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
