from collections import defaultdict

# Monotonic deque to keep max on window
# [1,2,1,0,4,2,6]
# k = 3

# size = 7
# until i = 4

# stack = [2, 1]
# 
 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        
        res = []
        
        cs = defaultdict(int)
        stack = []

        for i in range(size):
            cs[nums[i]] += 1
            
            if i < k - 1:
                continue
            
            res.append(max(list(cs.keys())))

            cs[nums[i - (k - 1)]] -= 1
            if cs[nums[i - (k - 1)]] == 0:
                cs.pop(nums[i - (k - 1)])
            

            
        
        return res
            
