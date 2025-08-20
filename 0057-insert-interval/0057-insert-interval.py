class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        merged = []
        newstart, newend = newInterval
        for i in range(len(intervals)):
            start, end = intervals[i]
          

            if end < newstart:
                merged.append([start, end])
            elif start > newend:
                merged.append([newstart, newend])
                newstart, newend = start, end

            else:
                newstart = min(newstart, start)
                newend = max(newend, end)

        merged.append([newstart, newend])
        return merged
                
            
            
            
