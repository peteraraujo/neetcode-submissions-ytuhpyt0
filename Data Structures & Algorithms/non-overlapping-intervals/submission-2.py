class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        size = len(intervals)

        prevend = intervals[0][1]
        res = 0

        for i in range(1, size):
            current = intervals[i]
            
            # Previous end is less or equals than current interval's start, so there is no overlap.
            if prevend <= current[0]:
                prevend = current[1]
                continue
            
            # Overlap
            res += 1
            prevend = min(prevend, current[1])
        
        return res

            
