def _validar_texto(*valores):
    for v in valores:
        if not isinstance(v, str):
            raise TypeError(f"Se esperaba str, se recibió {type(v).__name__}")


def reverse(s):
    _validar_texto(s)
    return s[::-1]


def count_vowels(s):
    _validar_texto(s)
    return sum(c in "aeiouáéíóúü" for c in s.lower())


def is_palindrome(s):
    _validar_texto(s)
    s = "".join(c for c in s.lower() if c.isalnum())
    return s == reverse(s)


def to_upper(s):
    _validar_texto(s)
    return s.upper()


def concat(a, b):
    _validar_texto(a, b)
    return a + b
