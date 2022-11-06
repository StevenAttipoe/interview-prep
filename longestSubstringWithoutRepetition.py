
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

def test_longestSubstringWithoutDuplication():
    actual = longestSubstringWithoutDuplication("clementisacap")
    expected = "mentisac"
    assert actual == expected