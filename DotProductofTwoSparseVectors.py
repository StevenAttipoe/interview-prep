from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for index, num in enumerate(nums):
            if num != 0:
                self.nonzeros[index] = num


    def dotProduct(self, vec: 'SparseVector') -> int:
        dotProduct = 0

        for key, val in self.nonzeros.items():
            if key in vec.nonzeros:
                dotProduct += val * vec.nonzeros[key]
        
        return dotProduct

class SparseVector2:
    def __init__(self, nums: List[int]):
        self.vector = nums

    def dotProduct(self, vec: 'SparseVector') -> int:
        dotProduct = 0

        for num1, num2 in zip(self.vector, vec.vector):
            dotProduct += num1 * num2
        
        return dotProduct
    

if __name__ == "__main__":
    v1 = SparseVector([1,0,0,2,3])
    v2 = SparseVector([0,3,0,4,0])
    result = v1.dotProduct(v2)
    assert(result == 8)

    v1 = SparseVector([0,1,0,0,0])
    v2 = SparseVector([0,0,0,0,2])
    result = v1.dotProduct(v2)
    assert(result == 0)

    v1 = SparseVector([0,1,0,0,2,0,0])
    v2 = SparseVector([1,0,0,0,3,0,4])
    result = v1.dotProduct(v2)
    assert(result == 6)