class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []

        res.append(intervals[0])

        print(res)
        
        for i in range(1, len(intervals)):

            current = intervals[i]

            if res[-1][1] >= current[0]:
                res[-1][1] = max(res[-1][1], current[1])
            else:
                res.append(current)

            print(current, res)
        
        return res





















        