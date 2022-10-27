# O(n * 2^n) time and O(n * 2^n) space
def subsets(nums):
    subsets = [[]]

    for num in nums:
        for i in range(len(subsets)):
            newSubset = [num] + subsets[i]
            subsets.append(newSubset)
            
    return subsets

subsets([1,2,3])
def test_subsets_with_one_input():
    actual = subsets([1])
    expected = [[], [1]]
    assert actual == expected

def test_subsets_with_two_input():
    output = subsets([1,2])
    assert([] in output)
    assert([1] in output)
    assert([2] in output)
    assert([1, 2] in output or [2,1] in output)

def test_subsets_with_three_input():
    output = subsets([1,2,3])
    assert([] in output)
    assert([1] in output)
    assert([2] in output)
    assert([1, 2] in output or [2,1] in output)
    assert([3] in output)
    assert([1, 3] in output or [3,1] in output)
    assert([2, 3] in output or [3,2] in output)
    assert([1, 2, 3] in output or [3,2,1] in output)


    #Algorithm:
    #    Add the each number to each element (subset) to the output list [[]]

    #nums = [1]
    # output = [[], [1]]

    # nums = [1,2]
    # output = [[], [1], [2], [1,2]]

    # nums = [1,2,3]
    # output = [[3], [1,3], [2,3], [1,2,3], [], [1], [2], [1,2]]

    #Observation: As we loop through the array, the output doubles
