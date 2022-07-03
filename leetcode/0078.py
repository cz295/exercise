class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ### backtracking
        res = []
        curr = []
        def backtrack(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
            backtrack(i + 1)
        backtrack(0)
        return res
        
        ### normal
        curr_res = [[]]
        for i in nums:
            curr_res += [
                x + [i] for x in curr_res
            ]
        return curr_res
