class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        size = len(intervals)

        res = []
        insertionPoint = size

        # Find insertion point.
        # Append intervals before new interval.
        for i in range(size):
            current = intervals[i]
            
            # Current interval's end is after new interval's start, so they are overlapping OR current interval is after new interval
            if current[1] >= newInterval[0]:
                insertionPoint = i
                break
            
            # Current interval is before new one.
            res.append(current)
        
        addFromHere = size

        # Merge overlapping intervals with new interval
        for i in range(insertionPoint, size):
            current = intervals[i]

            # If current is after new interval, there are no more overlapping intervals
            if newInterval[1] < current[0]:
                addFromHere = i
                break
            
            # Merge
            newInterval = [min(newInterval[0], current[0]), max(newInterval[1], current[1])]

        # Append new interval
        res.append(newInterval)

        # Add rest of intervals
        res.extend(intervals[addFromHere:])

        return res

