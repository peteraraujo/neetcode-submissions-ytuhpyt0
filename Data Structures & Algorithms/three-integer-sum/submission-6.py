class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = set()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            
            ni = nums[i]

            while l < r:
                nl = nums[l]
                nr = nums[r]
                
                temp = ni + nl + nr

                if temp == 0:
                    res.add((ni, nl, nr))
                    l += 1
                elif temp > 0:
                    r -= 1
                else:
                    l += 1
        
        return list([list(t) for t in res])