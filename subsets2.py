def powerset(nums, index=None):
    if index is None:
        index = len(nums) - 1
    if index < 0:
        return [[]]

    element = nums[index]
    subsets = powerset(nums, index - 1)

    for i in range(len(subsets)):
        newSubet = subsets[i] + [element]
        subsets.append(newSubet)

    return subsets

print(powerset([1,2]))
def test_subsets_with_one_input():
    actual = powerset([1])
    expected = [[], [1]]
    assert actual == expected

def test_subsets_with_two_input():
    output = powerset([1,2])
    assert([] in output)
    assert([1] in output)
    assert([2] in output)
    assert([1, 2] in output or [2,1] in output)