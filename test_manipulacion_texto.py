import pytest

from manipulacion_texto import concat, count_vowels, is_palindrome, reverse, to_upper


@pytest.mark.parametrize("s, esperado", [
    ("hola", "aloh"),
    ("", ""),
    ("a", "a"),
    ("ab c", "c ba"),
])
def test_reverse(s, esperado):
    assert reverse(s) == esperado


@pytest.mark.parametrize("s, esperado", [
    ("hola", 2),
    ("", 0),
    ("xyz", 0),
    ("AEIOU", 5),
    ("Canción", 3),
    ("pingüino", 4),
])
def test_count_vowels(s, esperado):
    assert count_vowels(s) == esperado


@pytest.mark.parametrize("s, esperado", [
    ("oso", True),
    ("", True),
    ("Reconocer", True),
    ("Anita lava la tina", True),
    ("hola", False),
])
def test_is_palindrome(s, esperado):
    assert is_palindrome(s) is esperado



