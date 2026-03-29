import heapq as h
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        h.heapify(self.nums)
        while len(self.nums) > k:
            h.heappop(self.nums)
        

    def add(self, val: int) -> int:
        h.heappush(self.nums, val)
        if len(self.nums) > self.k:
            h.heappop(self.nums)
        return self.nums[0]
        
