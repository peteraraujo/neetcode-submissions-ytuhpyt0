class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        
        size = len(nums)

        l = 0
        cursum = 0
        res = 0

        for i in range(size):
            
            if (i - 1 - l) + 1 == k:
                cursum -= nums[l]
                l += 1
            
            cursum += nums[i]
            if (i - l) + 1 == k and cursum / k >= threshold:
                res += 1
        
        return res