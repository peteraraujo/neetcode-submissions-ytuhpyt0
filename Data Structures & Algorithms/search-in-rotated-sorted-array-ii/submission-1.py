class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        size = len(nums)

        l, r = 0, size - 1

        while l < r:
            

            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1

            m = (l + r) // 2

            if nums[l] > nums[m]:
                r = m
            else:
                l = m + 1
        
        def bs(l, r):
            while l <= r:
                if nums[l] == nums[r]:
                    return l if nums[l] == target else -1
                
                m = (l + r) // 2

                if nums[m] == target:
                    return m

                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return -1

        return bs(0, l-1) != -1 or bs(l, size-1) != -1
