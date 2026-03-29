import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hq = list(map(lambda x:-x , nums))
        heapq.heapify(self.hq)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.hq, -val)
        temp = []
        for _ in range(self.k):
            temp.append(-heapq.heappop(self.hq))
        for t in temp:
            heapq.heappush(self.hq, -t)

        return temp[-1]
        
