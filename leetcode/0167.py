class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1, 2]
        else:
            first, second = 0, len(numbers) - 1
            curr_sum = numbers[first] + numbers[second]
            while curr_sum != target:
                if target > curr_sum:
                    first += 1
                else:
                    second -= 1
                curr_sum = numbers[first] + numbers[second]
            return [first + 1, second + 1]

