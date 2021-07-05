from random import choice as _choice
from string import ascii_letters as _ascii_letters
from string import digits as _digits
_sym = '!#$%&()*+,-./:;<=>?@[\\]^_`{|}~'


def gen_password(length: int = 8, use_numbers=True, use_symbols=True) -> str:
    """function that create a password

    Args:
        length (int, optional): how long to generate. Defaults to 8.
        use_numbers (bool, optional): use numbers?. Defaults to True.
        use_symbols (bool, optional): use symbols?. Defaults to True.

    Returns:
        str: the new password generated
    """
    _chars = _ascii_letters
    if use_numbers:
        _chars += _digits
    if use_symbols:
        _chars += _sym
    _password = ""
    for _ in range(length):
        _password += _choice(_chars)
    return _password
