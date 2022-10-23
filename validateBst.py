# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))
    
    
def validateBstHelper(node,min,max):
    if node is None:
        return True
    if node.value < min or node.value >= max:
        return False 
            
    return validateBstHelper(node.left,min,node.value) and validateBstHelper(node.right,node.value,max)

def test_validateBst():
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    assert validateBst(root) == True