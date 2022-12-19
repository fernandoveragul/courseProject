import hashlib
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
        return 'Class <SecretPassword> was created VV_403_ISaP'

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
            raise CustomExceptions.EmptyAnyLineEdit()
        else:
            pass

        check_done = CryptoPassword.__is_lowupcase_valid(word)
        length_done = 8 < len(word) < 16
        if check_done:
            if length_done:
                return all((check_done, length_done))
            else:
                raise CustomExceptions.SmallInputSecretWordError()
        else:
            raise CustomExceptions.InvalidSomeSymbolError()

    @staticmethod
    def __is_password_valid(password: str) -> bool:
        if password == '':
            raise CustomExceptions.EmptyAnyLineEdit()
        else:
            pass

        special_symbols_done = any((True if s in Dicts.special_symbols else False for s in password))
        numbers_symbol_done = any((True if s in Dicts.numbers_for_pass else False for s in password))
        lowup_case = CryptoPassword.__is_lowupcase_valid(password)
        length_password = 8 < len(password) < 32
        if lowup_case and special_symbols_done and numbers_symbol_done:
            if length_password:
                return all((special_symbols_done, numbers_symbol_done,
                            lowup_case, length_password))
            else:
                raise CustomExceptions.SmallInputPasswordError()
        else:
            raise CustomExceptions.InvalidSomeSymbolError()

    @staticmethod
    def __encoding_password_by_base(password: str) -> str:
        password_is_valid = CryptoPassword.__is_password_valid(password)
        secret_password = b64.b32encode(b64.b64encode(password.encode()))
        return b64.b16encode(secret_password).decode() if password_is_valid else ''

    @staticmethod
    def __decoding_password_by_base(password: str) -> str:
        secret_password = b64.b32decode(b64.b16decode(password.encode()))
        return b64.b64decode(secret_password).decode()

    @staticmethod
    def __encoding_secret_word_by_5(word: str) -> str:
        word_is_valid = CryptoPassword.__is_secret_word_valid(word)
        return hashlib.md5(word.encode(), usedforsecurity=True).hexdigest() if word_is_valid else ''

    @staticmethod
    def __join_values_pass_word(fin_word: str, fin_pass: str) -> str:
        """Method take hashing word and hashing password. Rerun word + password."""
        word = CryptoPassword.__encoding_secret_word_by_5(fin_word)
        pas = CryptoPassword.__encoding_password_by_base(fin_pass)
        return f'{word}@#$%{pas}'

    @classmethod
    def start(cls, /, coding: list[str, str] = None, decoding: str = None, is_origin: bool = True) -> str | None:
        secret = decoding.split('@#$%') if decoding is not None else decoding
        if is_origin is True:
            return CryptoPassword.__join_values_pass_word(*coding)
        elif is_origin is False:
            hash_word, password = secret
            hash_is_done = hash_word == CryptoPassword.__encoding_secret_word_by_5(coding[0])
            if hash_is_done:
                return CryptoPassword.__decoding_password_by_base(password)
            else:
                raise CustomExceptions.InvalidHashPassError()
