class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        right_side_view = []
        queue = deque([]) if root is None else deque([root])
        while len(queue) > 0:
            no_in_stack = len(queue)
            pop_node = None
            for i in range(no_in_stack):
                pop_node = queue.popleft()
                if pop_node.left is not None:
                    queue.append(pop_node.left)
                if pop_node.right is not None:
                    queue.append(pop_node.right)
            right_side_view.append(pop_node.val)
        return right_side_view
            
