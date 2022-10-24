
def getPermutations(nums):
    permutations = []

    #base case
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        #Remove each number from nums
        num = nums.pop(0)

        #Recuse new nums array
        perms = getPermutations(nums)
        
        
        for perm in perms:
            #Add popped number back to the permutation
            perm.append(num)
            
        permutations.extend(perms)
        nums.append(num)

    return permutations
        
def test_getPermutations():
    perms = getPermutations([1,2,3])
    assert (len(perms) == 6)
    assert([1, 2, 3] in perms)
    assert([1, 3, 2] in perms)
    assert([2, 1, 3] in perms)
    assert([2, 3, 1] in perms)
    assert([3, 1, 2] in perms)
    assert([3, 2, 1] in perms)
    