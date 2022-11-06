def repeatedSubstringPattern(s: str) -> bool:
    paddedString = "".join((s[1:], s[:-1]))
    return s in paddedString


def test_repeatedSubstringPattern():
    actual = repeatedSubstringPattern("abcabcabcabc")
    expected = True

    assert actual == expected

    actual = repeatedSubstringPattern("aba")
    expected = False

    assert actual == expected

