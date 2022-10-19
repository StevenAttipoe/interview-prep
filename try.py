from itertools import permutations
from re import search


def anagram(word, dictionary: dict):
    possible_arrangements = permutations(word)
    combination = ""
    for each_possibility in possible_arrangements:
        combination += dictionary.find(each_possibility)+","
    return combination[:-1]
