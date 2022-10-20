def findAnagrams(s: str, p: str):
    if len(p) > len(s): return []

    sCount, pCount = {}, {}

    for i in range(len(p)):
        sCount[s[i]] = 1 + sCount.get(s[i],0)
        pCount[p[i]] = 1 + pCount.get(p[i],0)

    output = [0] if sCount == pCount else []

    left = 0
    for right in range(len(p), len(s)):
        sCount[s[right]] = 1 + sCount.get(s[right],0)
        sCount[s[left]] -= 1

        if sCount[s[left]] == 0:
            sCount.pop(s[left])

        left += 1

        if sCount == pCount:
            output.append(left)
    return output
findAnagrams("cbaebabacd","abc")

def test_findAnagrams1():
    actual = findAnagrams("cbaebabacd","abc")
    expected = [0,6]
    assert actual == expected


def test_findAnagrams2():
    actual = findAnagrams("abab","ab")
    expected = [0,1,2]
    assert actual == expected

def test_findAnagrams3():
    actual = findAnagrams("aaaaaaaaaa","aaaaaaaaaaaaa")
    expected = []
    assert actual == expected