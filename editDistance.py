def minDistance(word1: str, word2: str) -> int:
    edits  = [[x for x in range(len(word1) + 1)] for y in range(len(word2) + 1)]

    for r in range(1, len(word2) + 1):
        edits[r][0] = edits[r - 1][0] + 1

        for c in range(1, len(word1) + 1):
            if word2[r - 1] == word1[c - 1]:
                edits[r][c] = edits[r - 1][c - 1]

            else:
                edits[r][c] = min(edits[r - 1][c - 1], edits[r - 1][c], edits[r][c - 1]) + 1


    for r in range(1,len(word2) + 1):
        for c in range(1, len(word1) +1):
            print(edits[r][c], end=" ")
        print("")
    
    print(edits[-1][-1])

minDistance("horse", "ros")