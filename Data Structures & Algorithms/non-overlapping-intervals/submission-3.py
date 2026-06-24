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
            # At this point, since there is an overlap, we need to remove either the current one or the previous one
            res += 1

            # We will remove the one that is longer, so there is more room for other intervals.
            # Since we are removing the longest one, we will keep track of the minimum end, as is the one we are choosing to keep.
            prevend = min(prevend, current[1])
        
        return res

            
