class BSTIterator:
    #O(h) space
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
            
    #O(1) average
    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        return self.stack != []


class BSTIterator:
    #O(n) space
    def __init__(self, root):
        self.stack = []
        def inOrderTraversal(root):
            if root:
                inOrderTraversal(root.right)
                self.stack.append(root.val)
                inOrderTraversal(root.left)
        inOrderTraversal(root)

     #O(1) 
    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return self.stack != []