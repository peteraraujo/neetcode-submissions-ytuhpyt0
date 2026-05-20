class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)

        l, r = 0, size - 1
        
        while l <= r:
            m = (l + r) // 2
            lv = nums[m - 1] if m - 1 >= 0 else float('-inf')
            rv = nums[m + 1] if m + 1 < size else float('-inf')
            mv = nums[m]

            if mv > lv and mv > rv:
                return m
            
            if rv > mv:
                l = m + 1
            else:
                r = m - 1