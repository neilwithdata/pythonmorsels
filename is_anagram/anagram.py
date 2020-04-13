import string
from collections import Counter
from unicodedata import normalize


def is_anagram(str1, str2):
    def clean_string(s):
        remove = string.whitespace + string.punctuation
        for c in remove:
            s = s.replace(c, '')

        s = ''.join(c for c in normalize('NFD', s) if c in string.ascii_letters)
        return s.lower()

    c1 = Counter(clean_string(str1))
    c2 = Counter(clean_string(str2))

    return c1 == c2
