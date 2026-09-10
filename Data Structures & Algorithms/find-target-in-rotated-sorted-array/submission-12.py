class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)

        l, r = 0, size - 1

        while l < r:
            m = (l + r) // 2

            mnum = nums[m]

            if mnum == target:
                return m

            if mnum > nums[r]:
                l = m + 1
            else:
                r = m
        
        lookOnFirst = target <= nums[-1]

        l, r = r if lookOnFirst else 0, size - 1 if lookOnFirst else r - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            
        return -1
