class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int: 
        if not intervals:
            return 0
        
        intervals.sort(key =lambda s : s[1])
        count = 0
        print(intervals)
        last_start, last_end = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < last_end:
                count += 1
                continue
                
            elif start >= last_end:
                last_end = end

        return count
