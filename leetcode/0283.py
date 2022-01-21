class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = [i for i, a in enumerate(nums) if a == 0]
        zero_no = 0
        for i in range(len(nums)):
            if zero_no < len(zero_index) and i > zero_index[zero_no]:
                zero_no += 1
            if zero_no > 0:
                nums[i - zero_no] = nums[i]
        for i in range(len(zero_index)):
            nums[-1 - i] = 0
