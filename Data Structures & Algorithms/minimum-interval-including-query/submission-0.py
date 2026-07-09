class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort(key=lambda interval: interval[0])

        points = [-1] * (10000 + 1)

        for s, e in intervals:
            length = (e - s) + 1
            for p in range(s, e + 1):
                points[p] = length if points[p] == -1 or length < points[p] else points[p]
        
        return [points[q] for q in queries]