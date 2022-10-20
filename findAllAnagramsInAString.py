# Given two strings s and p, return an array of all the start indices of p's anagrams in s.
#  You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters 
# of a different word or phrase, typically using all the original letters exactly once.

def findAnagrams(string: str, anagram: str):
    anagramsLength = len(anagram)
    sortedAnagram = sorted(anagram)
    anagramsIndices = []
    
    for indice in range(0, len(string) - anagramsLength + 1):
        currAnagram = []
        for i in range(indice, indice + anagramsLength):
            currAnagram.append(string[i])
            

        if sorted(currAnagram) == sortedAnagram:
            anagramsIndices.append(indice)
            
    return anagramsIndices

    #O(nLogn + O(m * m + nLogn))
    #Armotize O(m * m) or 0(m^2)
    # where n is the length of the anagram and m is the length of the string

def test_findAnagrams1():
    actual = findAnagrams("cbaebabacd","abc")
    expected = [0,6]
    assert actual == expected


def test_findAnagrams2():
    actual = findAnagrams("abab","ab")
    expected = [0,1,2]
    assert actual == expected
