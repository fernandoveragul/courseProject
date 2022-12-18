import sys
import pyperclip
import design
from design import resources
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
        self.btnAbout.clicked.connect(self.info_about_app)
        self.btnCoding.clicked.connect(self.__encoding_decoding)
        self.btnShow.clicked.connect(self.__change_show_mode)

    def __encoding_decoding(self):
        data: dict = self.__parse_values()
        self.lblOutput.setText('')
        try:
            pyperclip.copy(CryptoPassword.start(**data))
            self.enterSecterPassword.setText('')
            self.enterSecretWord.setText('')
            self.__message_successful_copy()
        except CustomExceptions.InvalidHashPassError as ex:
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)
        except CustomExceptions.InvalidSomeSymbolError as ex:
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)
        except CustomExceptions.SmallInputPasswordError as ex:
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)
        except CustomExceptions.EmptyAnyLineEdit as ex:
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)
        except CustomExceptions.SmallInputSecretWordError as ex:
            QtWidgets.QMessageBox.warning(self, "Ошибка", ex.__doc__)

    def __parse_values(self) -> dict[str: list,
                                str: str | None,
                                str: bool]:
        if self.chbDecoding.isChecked():
            sw, sp, is_or = self.enterSecretWord.text(), self.enterSecterPassword.text(), False  # DECODING IS TRUE
            return {'coding': [sw], 'decoding': sp, 'is_origin': is_or}
        else:
            swp, is_or = [self.enterSecretWord.text(), self.enterSecterPassword.text()], True  # DECODING IS FALSE
            return {'coding': swp, 'decoding': None, 'is_origin': is_or}

    def __change_show_mode(self):
        QtWidgets.QMessageBox.information(self, "Пароль и слово",
                                          f'СС[{self.enterSecretWord.text()[::-1]}]'
                                          f'\nСП[{self.enterSecterPassword.text()[::-1]}]')

    def __message_successful_copy(self):
        message = QtWidgets.QMessageBox()
        message.setWindowTitle('Шифровальщик паролей')
        # message.setIcon(QtWidgets.QMessageBox.Ok)
        message.setText(self.INFO_MESSAGE)
        message.exec_()

    def info_about_app(self):
        self.about_window = AboutApplication()
        self.about_window.showMaximized()


def main():
    application = QtWidgets.QApplication(sys.argv)
    window = CurrentApplication()
    application.setWindowIcon(QtGui.QIcon(":icon.png"))
    window.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()

    # for MSWindows
    # cd compile
    # pyinstaller -w -F -i "..\design\icon.ico" ..\main.py
