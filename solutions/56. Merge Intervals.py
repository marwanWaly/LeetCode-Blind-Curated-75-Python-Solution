class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for s, e in intervals[1:]:
            if s > res[-1][1]:
                res.append([s, e])
            else:
                res[-1][1] = max(res[-1][1], e)
        return res
