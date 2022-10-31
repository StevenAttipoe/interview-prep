#O(n^2) time and O(n) space
def threeNumberSum(array, targetSum):
    array.sort()
    tripletsSum = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            currSum = array[i] +  array[left] + array[right]

            if currSum == targetSum:
                tripletsSum.append([array[i], array[left], array[right]])
                left += 1
                right -= 1

            if currSum < targetSum:
                left += 1
                
            if currSum > targetSum:
                right -= 1

    return tripletsSum
            
def test_threeNumberSum():
    assert(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
