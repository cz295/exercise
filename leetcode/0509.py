class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        x1, x2 = 0, 1
        for i in range(1, n):
            x1, x2 = x2, x1 + x2
        return x2
            
