class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        last_e = intervals[0][1]
        res = 0
        for s, e in intervals[1:]:
            if s < last_e:
                res += 1
                last_e = min(last_e, e)
            else:
                last_e = e
        return res
