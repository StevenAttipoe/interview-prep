#O(n) time and O(1) space
def firstDuplicateValue(array):
    for num in array:
        index = abs(num) - 1
        if array[index] < 0:
            return abs(num)
        array[index] *= -1

    return -1

    #Map each num to an index by subtracting 1 from it to start from 0.
    #Check if the mapped number per the new index if negative (meaning its a duplicate) and return it
    #Negative each mapped number per the new index

#O(n) time and O(n) space
def firstDuplicateValue2(array):
    distinctValues = set()

    for num in array:
        if num in distinctValues:
            return num
        distinctValues.add(num)
    return -1

#O(n^2) time and O(1) space
def firstDuplicateValue3(array):
    minIndex = len(array)
    
    for i in range(len(array)):
        firstVal = array[i]

        for j in range(i+1, len(array)):
            secondVal = array[j]
            if firstVal == secondVal:
                minIndex = min(minIndex, j)

    return -1 if minIndex is len(array) else array[minIndex]
                



def test_firstDuplicateValue():
        input = [2, 1, 5, 2, 3, 3, 4]
        expected = 2

        actual = firstDuplicateValue2(input)
        assert(actual == expected)

        actual = firstDuplicateValue3(input)
        assert(actual == expected)

        actual = firstDuplicateValue(input)
        assert(actual == expected)