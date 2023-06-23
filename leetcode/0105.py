class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        in_index_map = dict(map(reversed, enumerate(inorder)))
        
        def build_tree(pre_start: int, in_start: int, in_end: int) -> tuple[TreeNode | None, int]:
            if in_start >= in_end: return None, pre_start
            
            root_val = preorder[pre_start]
            root_index = in_index_map[root_val]
            
            l_tree, pre_end = build_tree(pre_start + 1, in_start, root_index)
            r_tree, pre_end = build_tree(pre_end, root_index + 1, in_end)
            
            return TreeNode(root_val, l_tree, r_tree), pre_end
        
        return build_tree(0, 0, len(inorder))[0]
