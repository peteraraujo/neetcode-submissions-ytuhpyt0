class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)

        nums.sort()

        res = []
        for f in range(size - 2):

            if f > 0 and nums[f] == nums[f - 1]:
                continue
            
            l, r = f + 1, size - 1
            while l < r:
                summ = nums[f] + nums[l] + nums[r]
                
                
                if l != f + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                if r != size - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue

                if summ == 0:
                    res.append([nums[f], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    continue
                
                if summ < 0:
                    l += 1
                else:
                    r -= 1
        
        return res