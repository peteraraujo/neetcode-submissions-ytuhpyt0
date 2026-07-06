from heapq import heappop as hpop, heappush as hpush

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def _isEven(self):
        return ((len(self.left) + len(self.right)) % 2) == 0


    def addNum(self, num: int) -> None:

        hpush(self.left, -num)

        if len(self.left) - len(self.right) > 1:
            hpush(self.right, -hpop(self.left))
        
        if self.right and -self.left[0] > self.right[0]:
            ln = -hpop(self.left)
            rn = hpop(self.right)

            hpush(self.left, -rn)
            hpush(self.right, ln)


        

    def findMedian(self) -> float:
        print(self.left, self.right, self._isEven())
        if self._isEven():
            return ((-self.left[0] + self.right[0]) / 2)
        
        return -self.left[0]



        
        