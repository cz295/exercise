class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        else:
            res_ret = []
            for i, a in enumerate(nums):
                res_ret += [[a] + x for x in self.permute(nums[:i] + nums[i+1:])]
            return res_ret

    def permute(self, nums):
        result = []
        def recursion(unused, path):
            if len(unused) == 0:
                result.append(path[:])
                return
            for num in unused:
                next_unused = unused[:]
                next_unsed.remove(num)
                recursion(next_unused, path + [num])
        recusion(nums, [])
        return result
