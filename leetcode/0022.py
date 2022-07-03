class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_res = []
        def backtrack(_str, l, r):
            if l == n and r == n:
                all_res.append(_str)
            if r > l or l > n or r > n:
                return 
            else:
                backtrack(_str + '(', l + 1, r)
                backtrack(_str + ')', l, r + 1)
        backtrack('', 0, 0)
        return all_res
        
        
