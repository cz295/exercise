class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            print(nums, low, mid, high)
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        # counter = {i:0 for i in range(3)}        
        # for i in nums:
        #     counter[i] += 1
        # nums[:counter[0]] = [0] * counter[0]
        # nums[counter[0]: counter[0] + counter[1]] = [1] * counter[1]
        # nums[counter[0] + counter[1]:] = [2] * counter[2]
