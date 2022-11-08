#O(n) time and O(min(n, a)) a - set of unqiue alphabets
def longestSubstringWithoutDuplication(string):
    seen = {}
    longest = [0, 1]
    startIdx = 0

    for i,char in enumerate(string):
        if char in seen:
            startIdx = max(startIdx, seen[char] + 1)

        if longest[1] - longest[0] < i-startIdx+1:
            longest = [startIdx, i+1]
        
        seen[char] = i
    return string[longest[0]: longest[1]]

#O(n) time and O(min(n, a)) a - set of unqiue alphabets
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res

#O(n^3) time and O(min(n, a)) a - set of unqiue alphabets
def lengthOfLongestSubstring(s: str) -> int:
    def check(start, end):
        chars = set()
        for i in range(start, end + 1):
            c = s[i]
            if c in chars:
                return False
            chars.add(c)
        return True

    n = len(s)

    res = 0
    for i in range(n):
        for j in range(i, n):
            if check(i, j):
                res = max(res, j - i + 1)
    return res

def test_longestSubstringWithoutDuplication():
    actual = longestSubstringWithoutDuplication("clementisacap")
    expected = "mentisac"
    assert actual == expected