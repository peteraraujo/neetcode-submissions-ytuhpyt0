class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):
            interval = intervals[i]
            
            if interval[1] < toBeRemoved[0]:
                res.append(interval)
                continue
            
            elif toBeRemoved[1] <= interval[0]:
                res.append(interval)
                continue

            elif interval[0] >= toBeRemoved[0] and interval[1] <= toBeRemoved[1]:
                continue

            elif toBeRemoved[0] >= interval[0] and toBeRemoved[1] <= interval[1]:
                # Left
                if interval[0] != toBeRemoved[0]:
                    res.append([interval[0], toBeRemoved[0]])
                
                # Right
                if toBeRemoved[1] != interval[1]:
                    res.append([toBeRemoved[1], interval[1]])
            
            elif interval[0] < toBeRemoved[0]:
                res.append([interval[0], toBeRemoved[0]])
            elif toBeRemoved[1] < interval[1]:
                res.append([toBeRemoved[1], interval[1]])
        
        return res