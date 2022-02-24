class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 0 if n == 0 else 1
        x0, x1, x2 = 0, 1, 1
        for i in range(2, n):
            x0, x1, x2 = x1, x2, x0 + x1 + x2
        return x2
