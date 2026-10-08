def reverse(s):
    return s[::-1]


def count_vowels(s):
    return sum(c in "aeiouáéíóúü" for c in s.lower())


def is_palindrome(s):
    s = "".join(c for c in s.lower() if c.isalnum())
    return s == reverse(s)


def to_upper(s):
    return s.upper()


