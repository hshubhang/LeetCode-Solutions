class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()

        for i in range(len(intervals) - 1):
            start_time, end_time = intervals[i]

            if end_time > intervals[i+1][0]:
                return False

        return True