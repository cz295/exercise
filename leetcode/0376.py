class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        is_larger = 0
        no_wiggle = 1
        for prev, curr in zip(nums[:-1], nums[1:]):
            if curr > prev and is_larger != 1:
                no_wiggle += 1
                is_larger = 1
            if curr < prev and is_larger != -1:
                no_wiggle += 1
                is_larger = -1
        return no_wiggle
