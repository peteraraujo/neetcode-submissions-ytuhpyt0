from collections import deque

# Monotonic deque to keep max on window
# [1, -1]
# k = 3

# size = 7
#          1
# deque = [0]
# 
 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        
        res = []
        
        dq = deque()
        stack = []

        for i in range(size):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])
                if i - (k - 1) == dq[0]:
                    dq.popleft()
            
        
        return res
            
