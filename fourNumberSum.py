#O(n^4) time and O(n) space
def fourNumberSum(array, targetSum):
    quadruplets = []

    for firstIdx in range(len(array)):
        for secondIdx  in range(firstIdx + 1, len(array)):
            for thirdIdx  in range(secondIdx + 1, len(array)):
                for fourthIdx  in range(thirdIdx + 1, len(array)):
                    first, second, third, fourth = array[firstIdx], array[secondIdx], array[thirdIdx], array[fourthIdx]
                    sum = first + second + third + fourth
                    if sum == targetSum:
                        quadruplets.append([first, second, third, fourth])
                        print([first, second, third, fourth])
    return quadruplets if array is not None else None


#O(n^3) time and O(n^2) space
def fourNumberSum(array, targetSum):
    array.sort()
    quadruplets = []

    for firstIdx in range(len(array)):
        for secondIdx  in range(firstIdx + 1, len(array) - 2):
            left = secondIdx + 1
            right = len(array) - 1

            while left < right:
                first, second, third, fourth = array[firstIdx], array[secondIdx], array[left],  array[right]
                currentSum = first + second + third + fourth
                
                if currentSum == targetSum :
                    quadruplets.append([first, second, third, fourth])
                    left += 1
                    right -= 1
                
                if currentSum < targetSum:
                    left += 1
                if currentSum > targetSum:
                    right -= 1

    return quadruplets 


def sortAndStringify(array):
    return ",".join(sorted(list(map(lambda x: str(x), array))))


def test_case_1():
    output = fourNumberSum([7, 6, 4, -1, 1, 2], 16)
    output = list(map(sortAndStringify, output))
    quadruplets = [[7, 6, 4, -1], [7, 6, 1, 2]]
    assert(len(output) == 2)
    for quadruplet in quadruplets:
        assert(sortAndStringify(quadruplet) in output)