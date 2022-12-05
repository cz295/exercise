class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        res = [nums[0]]
        for val in nums[1:]:
            res.append(res[-1] + val)
        return res
