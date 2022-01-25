class Solution:
    def climbStairs(self, n: int) -> int:
        x0, x1 = 1, 1
        for i in range(2, n + 1):
            x0, x1 = x1, x0 + x1
        return x1

