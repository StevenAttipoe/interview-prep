def nestedListWeightSum(nestedList) -> int:
    def dfs(nestedList, depth):
        weightSum = 0
        for element in nestedList:
            if type(element) == list:
                weightSum += dfs(element, depth + 1)
            else:
                weightSum += int(element) * depth
        return weightSum
    return dfs(nestedList, 1)


result = nestedListWeightSum([[1,1],2,[1,1]])
assert(result == 10)


result = nestedListWeightSum([1,[4,[6]]])
assert(result == 27)
