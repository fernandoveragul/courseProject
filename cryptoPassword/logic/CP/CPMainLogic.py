import base64 as b64
from . import CPDictsLang as Dicts
from . import CPCustomExceptions as CustomExceptions


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
            ``Class.start(**data_??coding)``
    """

    def __repr__(self):
        return 'Class <CryptoPassword> was created LEVIATHAN EQUILIBRIST'

    def __call__(self):
        return False

    @staticmethod
    def __is_lowupcase_valid(any_word: str) -> bool:
        lowercase_symbols_done_en = any((True if s in Dicts.en_EN_dict else False for s in any_word))
        lowercase_symbols_done_ru = any((True if s in Dicts.ru_RU_dict else False for s in any_word))
        upper_symbols_done_en = any((True if s in Dicts.en_EN_dict.upper() else False for s in any_word))
        upper_symbols_done_ru = any((True if s in Dicts.ru_RU_dict.upper() else False for s in any_word))
        lowercase_symbols_done = any((lowercase_symbols_done_ru, lowercase_symbols_done_en))
        uppercase_symbols_done = any((upper_symbols_done_ru, upper_symbols_done_en))
        return all((lowercase_symbols_done, uppercase_symbols_done))

    @staticmethod
    def __is_secret_word_valid(word: str) -> bool:
        if word == '':
            raise CustomExceptions.EmptyAnyLineEdit

        if check_lowup_is_done := CryptoPassword.__is_lowupcase_valid(word):
            if length_done := 8 < len(word) < 16:
                return all((check_lowup_is_done, length_done))
            else:
                raise CustomExceptions.SmallInputSecretWordError
        else:
            raise CustomExceptions.InvalidLowUpCaseSecretWord

    @staticmethod
    def __is_password_valid(password: str) -> bool:
        if password == '':
            raise CustomExceptions.EmptyAnyLineEdit

        check_special_symbols_is_done = any((True if s in Dicts.special_symbols else False for s in password))
        check_numbers_symbol_is_done = any((True if s in Dicts.numbers_for_pass else False for s in password))

        if check_special_symbols_is_done is False:
            raise CustomExceptions.InvalidSpecialSymbolError

        if check_numbers_symbol_is_done is False:
            raise CustomExceptions.InvalidNumberSymbolError

        if check_lowup_is_done := CryptoPassword.__is_lowupcase_valid(password):
            if length_password := 8 < len(password) < 32:
                return all((check_special_symbols_is_done, check_numbers_symbol_is_done,
                            check_lowup_is_done, length_password))
            else:
                raise CustomExceptions.SmallInputPasswordError
        else:
            raise CustomExceptions.InvalidLowUpCasePassword

    @staticmethod
    def __encoding(message: str, *, is_password: bool) -> str:
        """
        ``Function encodes the received value``
        :param message: current message for encode
        :return: encoded message
        """
        if is_password:
            message_is_valid = CryptoPassword.__is_password_valid(message)
        else:
            message_is_valid = CryptoPassword.__is_secret_word_valid(message)

        encoded_message = b64.b32encode(b64.b64encode(message.encode()))
        return b64.b16encode(encoded_message).decode() if message_is_valid else ''

    @staticmethod
    def __decoding(message: str) -> str:
        """
        ``Function decodes the resulting value``
        :param message: current message for decoding
        :return: decoded message
        """
        secret_password = b64.b32decode(b64.b16decode(message.encode()))
        return b64.b64decode(secret_password).decode()

    @staticmethod
    def __join_values_pass_word(word: str, password: str) -> str:
        """
        ``The function glues two words``
        :param word: encoded secret word
        :param password: encoded password
        :return: word + password
        """
        word_ = CryptoPassword.__encoding(word, is_password=False)
        password_ = CryptoPassword.__encoding(password, is_password=True)
        return f'{word_}${password_}'

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
            return CryptoPassword.__join_values_pass_word(*coding)
        elif is_origin is False:
            word, password = decoding.split('$') if decoding is not None else decoding
            if word == CryptoPassword.__encoding(coding[0], is_password=False):
                return CryptoPassword.__decoding(password)
            else:
                raise CustomExceptions.InvalidSecretWordsError
