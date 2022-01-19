# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root 
        from collections import deque
        queue = deque([root])
        while True:
            len_queue = len(queue)
            cnt_none = 0
            for i in range(len_queue):
                pop_node = queue.popleft()
                if pop_node is not None:
                    queue.append(pop_node.right)
                    queue.append(pop_node.left)
                    pop_node.right, pop_node.left = pop_node.left, pop_node.right
                else:
                    cnt_none += 1
            if cnt_none == len_queue:
                break
        return root
