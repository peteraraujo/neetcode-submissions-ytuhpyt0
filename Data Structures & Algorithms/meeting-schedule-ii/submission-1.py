"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x.start)

        days = [intervals[0].end]

        for interval in intervals[1:]:
            for index, lastEndOfDay in enumerate(days):
                if lastEndOfDay <= interval.start:
                    days[index] = interval.end
                    added = True
                    break
            else:
                days.append(interval.end)
        
        return len(days)
                    
                





