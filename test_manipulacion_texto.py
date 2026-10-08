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



@pytest.mark.parametrize("s, esperado", [
    ("hola", "HOLA"),
    ("", ""),
    ("Hola Mundo 123", "HOLA MUNDO 123"),
    ("canción", "CANCIÓN"),
])
def test_to_upper(s, esperado):
    assert to_upper(s) == esperado


@pytest.mark.parametrize("a, b, esperado", [
    ("hola", "mundo", "holamundo"),
    ("", "abc", "abc"),
    ("abc", "", "abc"),
    ("", "", ""),
])
def test_concat(a, b, esperado):
    assert concat(a, b) == esperado


@pytest.mark.parametrize("funcion", [reverse, count_vowels, is_palindrome, to_upper])
@pytest.mark.parametrize("valor", [None, 123, ["a", "b"]])
def test_entrada_invalida(funcion, valor):
    with pytest.raises(TypeError):
        funcion(valor)


@pytest.mark.parametrize("a, b", [(1, 2), ("hola", None), (["a"], "b")])
def test_concat_entrada_invalida(a, b):
    with pytest.raises(TypeError):
        concat(a, b)