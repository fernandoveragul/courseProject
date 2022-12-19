class SmallInputPasswordError(Exception):
    """ОШИБКА: не выполнено ограничение на длину поля пароля, подробнее в справке"""


class SmallInputSecretWordError(Exception):
    """ОШИБКА: не выполнено ограничение на длину поля секретного слова, подробнее в справке"""


class InvalidLowUpCaseSecretWord(Exception):
    """ОШИБКА: не выполнено ограничение на верхний и нижний регистр символов секретного слова, подробнее в справке"""


class InvalidLowUpCasePassword(Exception):
    """ОШИБКА: не выполнено ограничение на верхний и нижний регистр символов секретного слова, подробнее в справке"""


class InvalidSpecialSymbolError(Exception):
    """ОШИБКА: не выполнено ограничение на особые символы в пароле, подробнее в справке"""


class InvalidNumberSymbolError(Exception):
    """ОШИБКА: не выполнено ограничение на цифры в пароле, подробнее в справке"""


class InvalidSecretWordsError(Exception):
    """ОШИБКА: секретные слова не совпадают, подробнее в справке"""


class EmptyAnyLineEdit(Exception):
    """ОШИБКА: одно из полей не было заполнено, подробнее в справке"""
