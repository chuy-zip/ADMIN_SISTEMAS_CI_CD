def reverse(s):
    return s[::-1]


def count_vowels(s):
    return sum(c in "aeiouáéíóúü" for c in s.lower())


