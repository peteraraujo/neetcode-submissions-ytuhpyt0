class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)

        res = 0

        l = 0
        cur = 0



        for r in range(size):

            cur += nums[r]

            while cur - nums[l] >= target:
                cur -= nums[l]
                l += 1
            
            if cur >= target:
                new = (r - l) + 1
                if res == 0:
                    res = new
                else:
                    res = min(res, new)
        
        return res

            