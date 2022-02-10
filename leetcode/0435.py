class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        remove_cnt = 0
        last_interval = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[last_interval][1]:
                last_interval = i
            else:
                remove_cnt += 1
                if intervals[i][1] < intervals[last_interval][1]:
                    last_interval = i
        return remove_cnt
