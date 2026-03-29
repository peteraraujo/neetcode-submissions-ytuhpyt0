class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        size = len(nums)

        l, r = max(nums), sum(nums)
        
        while l < r:
            m = (l + r) // 2

            count, cur = 1, 0

            for i in range(size):
                cur += nums[i]

                if cur > m:
                    count += 1
                    cur = nums[i]
            
            if count <= k:
                r = m
            else:
                l = m + 1
        
        return l