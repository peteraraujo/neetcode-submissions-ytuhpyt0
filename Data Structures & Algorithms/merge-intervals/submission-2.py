class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        size = len(intervals)
        intervals.sort(key=lambda item: item[0])

        res = [intervals[0]]

        for i in range(1, size):
            current = intervals[i]
            last = res[-1]
            
            # End of last is greater or equals to current's start, so there is an overlap
            if last[1] >= current[0]:
                # Merge
                res[-1][1] = max(last[1], current[1])
                continue
            
            res.append(current)
        
        return res
            

        

        
        