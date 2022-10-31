
#O(n) time and O(1) space (sliding window)
def strStr(haystack: str, needle: str) -> int:
    left, right = 0, len(needle)
    while right <= len(haystack):
        if haystack[left:right] == needle:
            return left
        left += 1
        right += 1
    return -1

#O(n) time and O(1) space
def strStr2(haystack: str, needle: str) -> int:
    haystackLen = len(haystack) 
    needleLen = len(needle)
    for i in range(haystackLen + 1 - needleLen):
        if haystack[i: i + needleLen] == needle:
            return i
    return -1

#O(n^2) time and O(1) space
def strStr4(haystack: str, needle: str) -> int:
    runningLength = 0
    for i in range(len(haystack) - len(needle)):
        runningLength = 0
        for j in range(len(needle)): 
            if haystack[i+j] == needle[j]:
                runningLength += 1
        if runningLength == len(needle):
            return i
    else:
        return -1

#O(n) time and O(1) space
def strStr3(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0
    if needle not in haystack:
        return -1
    return haystack.index(needle)




def test_strStr():
    actual = strStr4("hello", "ll")
    expected = 2
    assert (actual == expected)

    actual = strStr4("leetcode","leeto")
    expected = -1
    assert (actual == expected)

    actual = strStr4("a","a")
    expected = 0
    assert (actual == expected)