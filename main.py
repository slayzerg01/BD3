from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5 import uic, QtSql, QtCore
from PyQt5.QtSql import QSqlDatabase
import sys
from GPPForm import GPPForm


class mainWindow(QMainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        uic.loadUi("./ui/mainWindow.ui", self)
        self.db_init()
        self.GPPForm = None
        self.besedi_init()
        self.pushButtonGPP.clicked.connect(self.GPP_clk)
        self.tV_besedi.setModel(self.model_besedi)
        self.tV_besedi.hideColumn(self.model_besedi.fieldIndex("id_besedi"))
        self.tV_besedi.resizeColumnsToContents()
        self.tV_besedi.setItemDelegateForColumn(3, QtSql.QSqlRelationalDelegate(self.tV_besedi))
        self.tV_besedi.setItemDelegateForColumn(4, QtSql.QSqlRelationalDelegate(self.tV_besedi))
        self.pushButtonProv.clicked.connect(self.Prov_clk)
        self.pushButtonBes.clicked.connect(self.Bes_clk)

    def Bes_clk(self):
        self.stackedWidget.setCurrentWidget(self.page_1)

    def Prov_clk(self):
        self.stackedWidget.setCurrentWidget(self.page_2)

    def GPP_clk(self):
        if self.GPPForm is None:
            self.GPPForm = GPPForm()
        self.GPPForm.show()

    def db_init(self):
        self.db = QSqlDatabase().addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        self.db.setDatabaseName("gpp")
        self.db.setUserName("root")
        self.db.setPassword("qwerty123")
        if not self.db.open():
            QMessageBox.critical(self, "Ошибка!", self.db.lastError().text(), QMessageBox.Ok)

    def besedi_init(self):
        self.model_besedi = QtSql.QSqlRelationalTableModel(self)
        self.model_besedi.setTable("besedi")
        self.model_besedi.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model_besedi.setRelation(3, QtSql.QSqlRelation("sotr_gpp", "id_sotr_GPP", "FIO"))
        self.model_besedi.setRelation(4, QtSql.QSqlRelation("themes", "id_themes", "name"))
        self.model_besedi.select()
        self.model_besedi.setHeaderData(1, QtCore.Qt.Horizontal, "Дата беседы")
        self.model_besedi.setHeaderData(2, QtCore.Qt.Horizontal, "Охват")
        self.model_besedi.setHeaderData(3, QtCore.Qt.Horizontal, "Сотрудник ГПП")
        self.model_besedi.setHeaderData(4, QtCore.Qt.Horizontal, "Тема беседы")


def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
