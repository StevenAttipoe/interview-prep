class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(d) time | O(1) space d - depth (height) of the ancestor tree
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(topAncestor, descendantOne)
    depthTwo = getDescendantDepth(topAncestor, descendantTwo)
    
    while depthOne != depthTwo:
        if depthOne < depthTwo:
            descendantTwo = descendantTwo.ancestor
            depthTwo -= 1
        else:
            descendantOne = descendantOne.ancestor
            depthOne -= 1

    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
    
    return descendantOne

    
def getDescendantDepth(topAncestor, descendant):
    depth = 0
    
    while descendant != topAncestor:
        descendant = descendant.ancestor
        depth += 1

    return depth

class AncestralTreeTest(AncestralTree):
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTreeTest(letter)
    return ancestralTrees

new_trees()
def test_case_1():
    trees = new_trees()
    trees["A"].addDescendants(trees["B"], trees["C"])
    trees["B"].addDescendants(trees["D"], trees["E"])
    trees["D"].addDescendants(trees["H"], trees["I"])
    trees["C"].addDescendants(trees["F"], trees["G"])

    yca = getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
    assert (yca == trees["B"])
