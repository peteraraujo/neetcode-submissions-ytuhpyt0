import heapq as h
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        h.heapify(nums)

        res = 1

        for i in range(size):
            el = h.heappop(nums)
            if el <= 0:
                continue
            if el > res:
                return res
            if el == res:
                res += 1
        
        return res
