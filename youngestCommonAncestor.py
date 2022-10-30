class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(h) time | O(h) space d - depth (height) of the ancestor tree
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    ancestorHistory = set()

    while descendantOne != topAncestor:
        ancestorHistory.add(descendantOne.ancestor)
        descendantOne = descendantOne.ancestor

    while descendantTwo != topAncestor:
        if descendantTwo in ancestorHistory:
            return descendantTwo
        descendantTwo = descendantTwo.ancestor
    return topAncestor
    


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
