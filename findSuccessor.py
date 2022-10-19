class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, target):
    order = []
    getInOrderTraversal(tree,order)
    print(order)
    for index, node in enumerate(order):
        if (node.value == target.value and index+1 < len(order)):
            return order[index + 1]
            
    return None

def getInOrderTraversal(tree, order):
    if tree is None:
        return 

    getInOrderTraversal(tree.left,order)
    order.append(tree)
    getInOrderTraversal(tree.right,order)