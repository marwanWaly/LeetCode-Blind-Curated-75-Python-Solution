class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_s, new_e = newInterval
        res = []
        for ind, (s, e) in enumerate(intervals):
            if new_e < s:
                res.append([new_s, new_e])
                res += intervals[ind:]
                return res
            elif new_s > e:
                res.append([s, e])
            else:
                new_s = min(new_s, s)
                new_e = max(new_e, e)

        res.append([new_s, new_e])
        return res
