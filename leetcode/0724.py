class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        l_sum = 0
        l_sum_list = [0]
        for i in range(1, n):
            l_sum += nums[i - 1]
            l_sum_list.append(l_sum)
        total_sum = l_sum + nums[-1]
        for i in range(n):
            if 2 * l_sum_list[i] + nums[i] == total_sum:
                return i
        return -1

## others
##
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if((sum_nums - left_sum - nums[i]) == left_sum):
                return i
            left_sum += nums[i]

        return -1
