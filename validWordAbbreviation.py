def validWordAbbreviation(word: str, abbr: str) -> bool:
    i = j = 0
    abbrLen = 0

    while i < len(word) and j < len(abbr):
        if word[i] != abbr[j]:
            if abbr[j].isdigit():
                while j < len(abbr) and abbr[j].isdigit():
                    if abbrLen == 0 and abbr[j] == '0':
                        return False 
                    abbrLen = abbrLen * 10 + int(abbr[j])
                    j += 1
                
                i += abbrLen
                abbrLen = 0
            else:
                return False
        else:
            i += 1
            j += 1 

    return i == len(word) and j == len(abbr)
    

result  = validWordAbbreviation("internationalization", "i12iz4n")
assert(result == True)

result = validWordAbbreviation("apple", "a2e")
assert(result == False)

result = validWordAbbreviation("a", "01")
assert(result == False)

result = validWordAbbreviation("internationalization", "i5a11o1")
assert(result == True)
