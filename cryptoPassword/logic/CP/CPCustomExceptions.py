class SmallInputPasswordError(Exception):
    """ОШИБКА: не выполнено ограничение на длину поля пароля, подробнее в справке"""


class SmallInputSecretWordError(Exception):
    """ОШИБКА: не выполнено ограничение на длину поля секретного слова, подробнее в справке"""


class InvalidSomeSymbolError(Exception):
    """ОШИБКА: не выполнено ограничение на особые символы, подробнее в справке"""


class InvalidHashPassError(Exception):
    """ОШИБКА: секретные слова не совпадают, подробнее в справке"""


class EmptyAnyLineEdit(Exception):
    """ОШИБКА: одно из полей не было заполнено, подробнее в справке"""
