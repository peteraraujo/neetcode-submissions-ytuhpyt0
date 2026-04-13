from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.maxh = []
        self.minh = []

    def addNum(self, num: int) -> None:
        if not self.maxh or -self.maxh[0] >= num:
            heappush(self.maxh, -num)
        else:
            heappush(self.minh, num)
        
        
        if len(self.minh) > len(self.maxh):
            heappush(self.maxh, -heappop(self.minh))
        elif len(self.maxh) - len(self.minh) == 2:
            heappush(self.minh, -heappop(self.maxh))
        

    def findMedian(self) -> float:
        print(self.maxh, self.minh)
        if len(self.maxh) == len(self.minh):
            return (-self.maxh[0] + self.minh[0]) / 2
        else:
            return -self.maxh[0]
        
        
        
        