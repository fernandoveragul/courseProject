import sys
import design
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class Application(QtWidgets.QMainWindow, design.design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.startApp.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))  # Кнопка открывает следующую страницу
        self.exitApp.clicked.connect(self.close)  # Выход из приложения

        self.btnEx1_1.clicked.connect(lambda: self.example(chapter=1, example=1))
        self.btnEx1_2.clicked.connect(lambda: self.example(chapter=1, example=2))
        self.btnEx1_3.clicked.connect(lambda: self.example(chapter=1, example=3))
        self.btnEx1_4.clicked.connect(lambda: self.example(chapter=1, example=4))
        self.btnEx1_5.clicked.connect(lambda: self.example(chapter=1, example=5))

        self.btnEx2_1.clicked.connect(lambda: self.example(chapter=2, example=1))
        self.btnEx2_2.clicked.connect(lambda: self.example(chapter=2, example=2))
        self.btnEx2_3.clicked.connect(lambda: self.example(chapter=2, example=3))
        self.btnEx2_4.clicked.connect(lambda: self.example(chapter=2, example=4))

        self.btnEx3_1.clicked.connect(lambda: self.example(chapter=3, example=1))
        self.btnEx3_2.clicked.connect(lambda: self.example(chapter=3, example=2))
        self.btnEx3_3.clicked.connect(lambda: self.example(chapter=3, example=3))
        self.btnEx3_4.clicked.connect(lambda: self.example(chapter=3, example=4))
        self.btnEx3_5.clicked.connect(lambda: self.example(chapter=3, example=5))
        self.btnEx3_6.clicked.connect(lambda: self.example(chapter=3, example=6))
        self.btnEx3_7.clicked.connect(lambda: self.example(chapter=3, example=7))
        self.btnEx3_8.clicked.connect(lambda: self.example(chapter=3, example=8))
        self.btnEx3_9.clicked.connect(lambda: self.example(chapter=3, example=9))

        self.btnEx4_1.clicked.connect(lambda: self.example(chapter=4, example=1))

        self.btnEx5_1.clicked.connect(lambda: self.example(chapter=5, example=1))
        self.btnEx5_2.clicked.connect(lambda: self.example(chapter=5, example=2))
        self.btnEx5_3.clicked.connect(lambda: self.example(chapter=5, example=3))
        self.btnEx5_4.clicked.connect(lambda: self.example(chapter=5, example=4))
        self.btnEx5_5.clicked.connect(lambda: self.example(chapter=5, example=5))
        self.btnEx5_6.clicked.connect(lambda: self.example(chapter=5, example=6))

        self.pushButton.clicked.connect(self.printers)

    def example(self, *, chapter: int, example: int) -> None:
        """
        Args:
            chapter: Глава книги
            example: Практическое задание из книги

        Returns:

        """
        with open(fr"Examples\Example_{chapter}_{example}.html", "r", encoding='utf8') as file:
            html = file.read()

        self.Example.setHtml(html)

    def printers(self) -> None:
        """
        Открывает диалоговое окно для выбора печати
        Returns:

        """
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.Example.print_(printer)



if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.setWindowIcon(QtGui.QIcon(":icon.png"))
    window.showMaximized()
    sys.exit(application.exec_())
