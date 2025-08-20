class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            last_start, last_end = res[-1]
            start, end = intervals[i]
            if start <= last_end:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])

        return res