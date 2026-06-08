class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)

        l, r = 0, size - 1
        while l < r:
            m = (l + r) // 2
            
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        # smallest will be nums[r]
        if target <= nums[-1]:
            # search from r

            l, r = r, size - 1
            
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        
        else:
            l, r = 0, r - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1