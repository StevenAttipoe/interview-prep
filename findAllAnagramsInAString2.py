#O(n*nlogn)

def findAnagrams(string: str, anagram: str):
    sortedAnagram = sorted(anagram)
    index = 0
    curr_anagram = []
    output = []

    for letter in string:
        curr_anagram.append(letter)

        if len(curr_anagram) == len(anagram):
            
            if sorted(curr_anagram) == sortedAnagram:
                output.append(index)

            curr_anagram = curr_anagram[1:]
            index += 1

    return output
    
def test_findAnagrams1():
    actual = findAnagrams("cbaebabacd","abc")
    expected = [0,6]
    assert actual == expected


def test_findAnagrams2():
    actual = findAnagrams("abab","ab")
    expected = [0,1,2]
    assert actual == expected