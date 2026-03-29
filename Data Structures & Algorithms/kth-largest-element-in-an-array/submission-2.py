import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)

        for index, num in enumerate(heapq.nlargest(k, nums)):
            if index == k - 1:
                return num