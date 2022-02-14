class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[1])
        res = 1
        
        maxx = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > maxx:
                maxx = points[i][1]
                res += 1
        return res
        
        cnt = len(points)
        points.sort(key=lambda x: (x[1], x[0]))
        curr = points[0]
        for i in range(1, len(points)):
            if curr[1] >= points[i][0]:
                cnt -= 1
                curr = (min(points[i][0], curr[0]), curr[1])
            else:
                curr = points[i]
        return cnt
