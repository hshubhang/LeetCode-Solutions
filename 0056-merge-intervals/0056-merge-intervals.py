class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            last_start, last_end = res[-1]

            if start <= last_end:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])

        return res