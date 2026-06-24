"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda item: item.start)   
        rooms = []
        
        for interval in intervals:
            
            added = False
            
            for room in rooms:
                if room[-1].end <= interval.start:
                    room.append(interval)
                    added = True
                    break
            
            if added:
                continue
            
            rooms.append([interval])


        return len(rooms)