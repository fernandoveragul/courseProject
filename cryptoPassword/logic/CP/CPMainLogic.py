import base64 as b64
from . import CPDictsLang as Dicts
from . import CPCustomExceptions as CustomEx


class CryptoPassword:
    """
    ``Method CryptoPassword.start() can take dictionary with syntax sugar:``
            ``data_encoding = {``
                ``'coding': ['word', 'password'],``
                ``'decoding': None,``
                ``'is_origin': True``
                ``}``
            ``data_decoding = {``
                ``'coding': ['word'],``
                ``'decoding': 'decoding_pass',``
                ``'is_origin': False``
                ``}``
            ``Class.start(**data_encoding)``
            ``OR``
            ``Class.start(**data_decoding)``
    """

    def __repr__(self):
        return 'Class <CryptoPassword> was created LEVIATHAN EQUILIBRIST'

    def __call__(self):
        return False

    @classmethod
    def __is_lowupcase_valid(cls, message: str, *, is_password: bool) -> bool:
        lowercase_symbols_done_en = any((True if s in Dicts.en_EN_dict else False for s in message))
        lowercase_symbols_done_ru = any((True if s in Dicts.ru_RU_dict else False for s in message))

        upper_symbols_done_en = any((True if s in Dicts.en_EN_dict.upper() else False for s in message))
        upper_symbols_done_ru = any((True if s in Dicts.ru_RU_dict.upper() else False for s in message))

        lowercase_symbols_done = any((lowercase_symbols_done_ru, lowercase_symbols_done_en))
        uppercase_symbols_done = any((upper_symbols_done_ru, upper_symbols_done_en))

        if is_valid := all((lowercase_symbols_done, uppercase_symbols_done)):
            return is_valid
        else:
            raise CustomEx.InvalidLowUpCasePassword if is_password else CustomEx.InvalidLowUpCaseSecretWord

    @classmethod
    def __check_special_symbols(cls, message: str) -> bool:
        is_done = []
        for i in message:
            is_done.append(True if i in Dicts.special_symbols else False)

        if is_valid := any(is_done):
            return is_valid
        else:
            raise CustomEx.InvalidSpecialSymbolError

    @classmethod
    def __check_arabic_numbers(cls, message: str) -> bool:
        is_done = []
        for i in message:
            is_done.append(True if i in Dicts.numbers_for_pass else False)

        if is_valid := any(is_done):
            return is_valid
        else:
            raise CustomEx.InvalidNumberSymbolError

    @classmethod
    def __is_secret_word_valid(cls, word: str) -> bool:
        if word == '':
            raise CustomEx.EmptyAnyLineEdit

        if check_lowup_is_done := cls.__is_lowupcase_valid(word, is_password=False):
            if length_done := 8 < len(word) < 16:
                return all((check_lowup_is_done, length_done))
            else:
                raise CustomEx.SmallInputSecretWordError

    @classmethod
    def __is_password_valid(cls, password: str) -> bool:
        if password == '':
            raise CustomEx.EmptyAnyLineEdit

        if check_lowup_is_done := cls.__is_lowupcase_valid(password, is_password=True):
            if length_password := 8 < len(password) < 32:
                is_valid = all((cls.__check_special_symbols(password), cls.__check_arabic_numbers(password),
                                check_lowup_is_done, length_password))
                return is_valid
            else:
                raise CustomEx.SmallInputPasswordError

    @classmethod
    def __encoding(cls, message: str, *, is_password: bool) -> str:
        """
        ``Function encodes the received value``
        :param message: current message for encode
        :return: encoded message
        """

        if is_password:
            message_is_valid = cls.__is_password_valid(message)
        else:
            message_is_valid = cls.__is_secret_word_valid(message)

        encoded_message = b64.b85encode(b64.a85encode(message.encode()))
        return encoded_message.decode() if message_is_valid else ''

    @classmethod
    def __decoding(cls, message: str) -> str:
        """
        ``Function decodes the resulting value``
        :param message: current message for decoding
        :return: decoded message
        """
        secret_password = b64.a85decode(b64.b85decode(message.encode()))
        return secret_password.decode()

    @classmethod
    def __join_values_pass_word(cls, word: str, password: str) -> str:
        """
        ``The function glues two words``
        :param word: encoded secret word
        :param password: encoded password
        :return: word + password
        """

        word_ = cls.__encoding(word, is_password=False)
        password_ = cls.__encoding(password, is_password=True)
        return f'{word_}№{password_}'

    @classmethod
    def start(cls, /, coding: list[str, str] = None, decoding: str = None, is_origin: bool = True) -> str | None:
        """
        ``API function for use CryptoPassword``
        :param coding: list strings(secret_word, password) for encoding
        :param decoding: string for decoding or NULL
        :param is_origin: if True, then encoding. If False, then decoding
        :return: encoded of decoded message
        """

        if is_origin is True:
            return cls.__join_values_pass_word(*coding)
        elif is_origin is False:
            word, password = decoding.split('№') if decoding is not None else decoding
            if word == cls.__encoding(coding[0], is_password=False):
                return cls.__decoding(password)
            else:
                raise CustomEx.InvalidSecretWordsError
