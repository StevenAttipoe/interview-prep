from collections import Counter


def checkInclusion(self, s1: str, s2: str) -> bool:
    start, end = 0, len(s1)
    
    for i in range(len(s2) + 1 - len(s1)):
        if Counter(s2[start:end]) == Counter(s1):
            return True
        start += 1
        end += 1
    return False

print(checkInclusion("ab", "eidboaoo"))