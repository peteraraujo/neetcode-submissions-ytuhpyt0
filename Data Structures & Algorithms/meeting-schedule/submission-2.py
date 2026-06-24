"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key=lambda item: item.start)
        size = len(intervals)

        for i in range(1, size):
            current = intervals[i]
            prev = intervals[i - 1]
            
            if prev.end > current.start:
                return False
        
        return True

