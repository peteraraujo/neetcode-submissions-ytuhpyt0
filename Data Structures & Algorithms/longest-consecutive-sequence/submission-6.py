class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n log n). Space: O(1)
        # Time: O(n). Space: O(n)

        if not nums:
            return 0
        
        size = len(nums)
        nums.sort()

        res = count = 1
        cur = nums[0]

        for i in range(1, size):
            n = nums[i]
            if n == cur:
                continue
            
            if n == cur + 1:
                count += 1
                res = max(res, count)
            else:
                count = 1
            
            cur = n
        
        return res
