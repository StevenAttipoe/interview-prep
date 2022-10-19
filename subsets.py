class Solution:
    def subsets(nums):
        output = [[]]
        
        for num in nums:
            # Add the number and the permutations of that number 
            # and the other numbers in the output list
            output += [curr + [num] for curr in output]

        print(output)

        return output 

Solution.subsets([1,2,3])