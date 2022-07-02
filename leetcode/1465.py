class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        h_cuts = max([y - x for x, y in zip([0] + horizontalCuts, horizontalCuts + [h])])
        v_cuts = max([y - x for x, y in zip([0] + verticalCuts, verticalCuts + [w])])
        return (h_cuts * v_cuts) % (10 ** 9 + 7)
