# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if root is None:
            return 0
        _queue = deque([root])
        depth = 0
        while _queue:
            depth += 1
            queue_len = len(_queue)
            for i in range(queue_len):
                node = _queue.popleft()
                if node.left:
                    _queue.append(node.left)
                if node.right:
                    _queue.append(node.right)
        return depth
        
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
