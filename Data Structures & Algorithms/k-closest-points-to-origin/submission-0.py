from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []

        for point in points:

            distance = sqrt((0 - point[0])**2 + (0 - point[1])**2)
            heapq.heappush(minHeap, (distance, point))
        
        return [heapq.heappop(minHeap)[1] for _ in range(k)]