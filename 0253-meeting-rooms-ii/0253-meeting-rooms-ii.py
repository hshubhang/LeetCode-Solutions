class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:       
        if not intervals:
            return 0
        intervals.sort()
        end_times = []
        heapq.heapify(end_times)

        heapq.heappush(end_times, intervals[0][1])
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start >= end_times[0]:
                heapq.heappop(end_times)

            heapq.heappush(end_times, end)

        return len(end_times) 

        

        