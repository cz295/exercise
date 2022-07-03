class Solution:
    def countBits(self, n: int) -> List[int]:
        if n <= 2:
            res = [0, 1, 1][:n+1]
        else:
            res = [0] * (n + 1)
            res[:3] = [0, 1, 1]
            for i in range(2, n + 1):
                if i % 2 == 0:
                    res[i] = res[i//2]
                else:
                    res[i] = res[i//2] + 1
        return res

    # ref
    def countBits(self, n: int) -> List[int]:
        counter = [0]
        for i in range(1, n+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
