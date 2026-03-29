class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            n = nums[m]

            if n == target:
                return m

            if n > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1