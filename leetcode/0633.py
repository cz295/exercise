class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        max_val = math.floor(math.sqrt(c))
        val1, val2 = 0, max_val
        while val1 <= val2:
            total_val = val1 * val1 + val2 * val2 
            if total_val > c:
                val2 -= 1
            elif total_val < c:
                val1 += 1
            else:
                return True
        return False
