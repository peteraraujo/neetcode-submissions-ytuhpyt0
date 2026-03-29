import heapq as hp

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.lst = []
        self.k = k

        for num in nums:
            if len(self.lst) >= k:
                hp.heappushpop(self.lst, num)
            else:
                hp.heappush(self.lst, num)

    def add(self, val: int) -> int:
        if len(self.lst) >= self.k:
            hp.heappushpop(self.lst, val)
        else:
            hp.heappush(self.lst, val)
        return self.lst[0]
        
