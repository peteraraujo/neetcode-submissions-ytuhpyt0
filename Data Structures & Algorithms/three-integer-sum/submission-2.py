class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        if nums[0] > 0 or nums[-1] < 0:
            return []

        s = 0
        res = []

        while s < len(nums) - 2 and nums[s] <= 0:
            
            l = s + 1
            r = len(nums) - 1
            
            while l < r:
                total = nums[s] + nums[l] + nums[r]

                if total == 0:
                    res.append([nums[s], nums[l], nums[r]])
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    r -= 1
                elif total < 0:
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                else:
                    while l < r - 1 and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
            
            while s + 1 < len(nums) - 2 and nums[s + 1] == nums[s]:
                s += 1
            s += 1
        return res




