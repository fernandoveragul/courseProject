import sys
import pyperclip
import design
from logic.CP import *
from PyQt5 import QtWidgets, QtGui


class AboutApplication(QtWidgets.QWidget, design.about_design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class CurrentApplication(QtWidgets.QMainWindow, design.main_design):
    INFO_MESSAGE = 'ИНФОРМАЦИЯ БЫЛА СКОПИРОВАНА В БУФЕР ОБМЕНА'

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.about_window = None
        self.btnAbout.clicked.connect(self.__info_about_app)
        self.btnCoding.clicked.connect(self.__encoding_decoding)
        self.btnShow.clicked.connect(self.__show_data)

        self.chbDecoding.pressed.connect(self.__change_text)

        # ToolTips:
        self.btnShow.setToolTip('Кнопка "ПОКАЗАТЬ" выводит сообщение\nс введёнными секретным словом и паролем')
        self.btnAbout.setToolTip('Кнопка "СПРАВКА" открывает окно справки')
        self.btnCoding.setToolTip('Кнопка "КОДИРОВАНИЕ" кодирует/декодирует сообщение')
        self.chbDecoding.setToolTip('Чтобы выполнить декодирование сообщения установите галочку')
        self.enterSecretWord.setToolTip("Введите секретное слово, правила написания описаны в справке")
        self.enterSecterPassword.setToolTip("Введите пароль, правила написания описаны в справке")

    def __encoding_decoding(self) -> None:
        """
        ``The function encodes/decodes password and secret word, and also handles errors``
        """
        data: dict = self.__take_values()
        self.lblOutput.setText('')
        try:
            pyperclip.copy(CryptoPassword.start(**data))
            self.enterSecterPassword.setText('')
            self.enterSecretWord.setText('')
            QtWidgets.QMessageBox.information(self, "Успешно", self.INFO_MESSAGE)
        except CustomExceptions.InvalidSecretWordsError as ex:
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)  # Error handling without
        except CustomExceptions.InvalidSpecialSymbolError as ex:          # stopping the program cycle
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)
        except CustomExceptions.InvalidLowUpCasePassword as ex:
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)
        except CustomExceptions.InvalidLowUpCaseSecretWord as ex:
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)
        except CustomExceptions.InvalidNumberSymbolError as ex:
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)
        except CustomExceptions.SmallInputPasswordError as ex:
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)
        except CustomExceptions.EmptyAnyLineEdit as ex:
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)
        except CustomExceptions.SmallInputSecretWordError as ex:
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)

    def __take_values(self) -> dict[str: list, str: str | None, str: bool]:
        """
        ``Function takes values from lineEdits``

        :return: Dictionary, for use of syntactic sugar
        """

        if self.chbDecoding.isChecked():
            word, password = self.enterSecretWord.text(), self.enterSecterPassword.text()  # DECODING
            return {'coding': [word], 'decoding': password, 'is_origin': False}
        else:
            word_and_password = [self.enterSecretWord.text(), self.enterSecterPassword.text()]  # ENCODING
            return {'coding': word_and_password, 'decoding': None, 'is_origin': True}

    def __show_data(self) -> None:
        QtWidgets.QMessageBox.information(self, "Пароль и слово",
                                          f'С${self.enterSecretWord.text()[::-1]}'
                                          f'\nП${self.enterSecterPassword.text()[::-1]}')

    def __info_about_app(self) -> None:
        """
        ``Function make show about window``
        """
        self.about_window = AboutApplication()
        self.about_window.showMaximized()

    def __change_text(self):
        if self.chbDecoding.text() == "ДЕКОДИРОВАНИЕ":
            self.enterSecterPassword.setPlaceholderText("Введите зашифрованный пароль")
            self.chbDecoding.setText("КОДИРОВАНИЕ")
        else:
            self.chbDecoding.setText("ДЕКОДИРОВАНИЕ")
            self.enterSecterPassword.setPlaceholderText("Введите пароль")


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    application.setWindowIcon(QtGui.QIcon(":icon.png"))
    window = CurrentApplication()
    window.move(window.geometry().center())
    window.show()
    sys.exit(application.exec_())
