class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        plus = 1
        for i in range(n - 1, -1, -1):
            if plus == 1 and digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                plus = 0
                break
        if plus == 1:
            return [1] + digits
        else:
            return digits
        
