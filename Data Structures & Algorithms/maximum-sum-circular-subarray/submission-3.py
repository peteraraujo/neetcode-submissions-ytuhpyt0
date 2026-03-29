class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        size = len(nums)

        t = cmin = cmax = 0
        gmin = gmax = nums[0]

        for n in nums:
            t += n
            # max
            cmax = max(0, cmax) + n
            gmax = max(gmax, cmax)

            # min
            cmin = min(0, cmin) + n
            gmin = min(gmin, cmin)
        
        return gmax if gmax < 0 else max(gmax, t - gmin)



        

            


            


