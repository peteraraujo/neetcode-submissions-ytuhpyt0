class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)

        dq = deque()
        res = []

        def add(n):
            
            while dq and dq[-1] < n:
                dq.pop()
            
            dq.append(n)

        for i in range(k - 1):
            add(nums[i])

        for r in range(k - 1, size):
            add(nums[r])

            res.append(dq[0])

            if dq[0] == nums[r - (k - 1)]:
                dq.popleft()
        
        return res
