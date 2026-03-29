class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        
        l, r = 0, size - 1

        def bs(l, r):
            if l >= size:
                return -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        if nums[l] < nums[r]:
            return bs(l, r)

        
        while l < r:
            m = (l + r) // 2
            if nums[l] == nums[m]:
                break
            elif nums[l] < nums[m]:
                l = m
            else:
                r = m
        
        res = max(bs(0, l), bs(l+1, size - 1))
        return res