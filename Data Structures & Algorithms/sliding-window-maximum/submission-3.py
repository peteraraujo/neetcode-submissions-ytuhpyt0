from collections import defaultdict

# Monotonic stack to keep max on window
# [1,2,1,0,4,2,6]
# k = 3

# size = 7
# until i = 4
 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)

        if size < 2:
            return nums
        if k == size:
            return [max(nums)]
        
        res = []
        
        cs = defaultdict(int)

        for i in range(size):
            cs[nums[i]] += 1
            
            if i < k - 1:
                continue
            
            res.append(max(list(cs.keys())))

            cs[nums[i - (k - 1)]] -= 1
            if cs[nums[i - (k - 1)]] == 0:
                cs.pop(nums[i - (k - 1)])
            

            
        
        return res
            
