
def subsets(nums):
    output = [[]]
    
    for num in nums:
        # Add the number and the permutations of that number 
        # and the other numbers in the output list
        output += [curr + [num] for curr in output]
    return output 


def test_subsets_with_one_input():
    actual = subsets([1])
    expected = [[], [1]]
    assert actual == expected

def test_subsets_with_two_input():
    actual = subsets([1,2])
    expected = [[], [1], [2], [1, 2]]
    assert actual == expected

def test_subsets_with_three_input():
    actual = subsets([1,2,3])
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert actual == expected

#python3 -m pytest subsets.py -v

    #nums = [1]
    # output = [[], [1]]

    # nums = [1,2]
    # output = [[], [1], [2], [1,2]]

    # nums = [1,2,3]
    # output = [[3], [1,3], [2,3], [1,2,3], [], [1], [2], [1,2]]