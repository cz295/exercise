class Solution:
    # 1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {
            target - a: i for i, a in enumerate(nums)
        }
        for i, a in enumerate(nums):
            if a in num_dict and i != num_dict[a]:
                return [i, num_dict[a]]
