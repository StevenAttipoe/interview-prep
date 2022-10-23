

def getPermutations(array):
    if len(array) == 0:
        return []
    
    permutations = getPermutationsHelper(array)
    print(permutations)

    return permutations

def getPermutationsHelper(array, output=[]):
    output.append(array[:])
    print("out:",output)

    for i in range(0, len(array) - 1 ):
        perm = array
        swap(i, i + 1, perm)
        output.append(perm[:])
        print(output)

    return output

def swap(i, j, array):
    temp  = array[i]
    array[i] = array[j]
    array[j] = temp
    return array


def test_getPermutations():
    actual = getPermutations([1,2,3])
    expected = [[1, 2, 3],[1, 3, 2],[2, 1, 3],[2, 3, 1],[3, 1, 2],[3, 2, 1]]

    assert actual == expected