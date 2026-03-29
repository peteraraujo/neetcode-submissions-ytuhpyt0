class MedianFinder:

    def __init__(self):
        self.maxLeftHeap = []
        self.minRightHeap = []
        

    def addNum(self, num: int) -> None:

        maxLeftHeap = self. maxLeftHeap
        minRightHeap = self.minRightHeap

        if not maxLeftHeap or num <= -maxLeftHeap[0]:
            heapq.heappush(maxLeftHeap, -num)
        else:
            heapq.heappush(minRightHeap, num)

        diff = len(maxLeftHeap) - len(minRightHeap)
        if diff == 2:
            heapq.heappush(minRightHeap, -(heapq.heappop(maxLeftHeap)))
        elif diff == -2:
            heapq.heappush(maxLeftHeap, -(heapq.heappop(minRightHeap)))

    def findMedian(self) -> float:

        maxLeftHeap = self. maxLeftHeap
        minRightHeap = self.minRightHeap

        if len(maxLeftHeap) == len(minRightHeap):
            return (minRightHeap[0] + (-maxLeftHeap[0])) / 2
        elif len(maxLeftHeap) > len(minRightHeap):
            return -maxLeftHeap[0]
        else:
            return minRightHeap[0]
        