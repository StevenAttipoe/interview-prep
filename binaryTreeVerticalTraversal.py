# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from ast import List
from collections import defaultdict, deque
from typing import Optional

from maxWidthBT import TreeNode


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        columnTable = defaultdict(list)
        minCol = maxCol = 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)

                minCol = min(minCol, column)
                maxCol = max(maxCol, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))


        return [columnTable[i] for i in range(minCol, maxCol + 1)]

    def verticalOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[i] for i in sorted(columnTable.keys())]
