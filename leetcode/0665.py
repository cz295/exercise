class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        n = len(nums)
        cnt = 0
        curr_high = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if i == n - 1:
                    cnt += 1
                else:
                    if nums[i + 1] < nums[i - 1]:
                        if nums[i + 1] < nums[i]:
                            return False
                        else:
                            if nums[i + 1] >= curr_high and nums[i] >= curr_high:
                                cnt += 1
                                curr_high = nums[i]
                            else:
                                return False
                    else:
                        cnt += 1
                        curr_high = nums[i - 1]
            else:
                curr_high = nums[i - 1]
            if cnt >= 2:
                return False
        return True
