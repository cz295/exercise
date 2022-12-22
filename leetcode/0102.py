# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if root is None:
            return []
        stack = deque([root])
        level_count = 1
        res = []
        while stack:
            level = []
            new_count = 0
            for i in range(level_count):
                x = stack.popleft()
                level.append(x.val)
                if x.left:
                    stack.append(x.left)
                    new_count += 1
                if x.right:
                    stack.append(x.right)
                    new_count += 1
            level_count = new_count
            res.append(level)
        return res



