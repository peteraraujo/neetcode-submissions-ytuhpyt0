class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n log n). Space: O(1)
        # Time: O(n). Space: O(n)

        if not nums:
            return 0

        res = 1
        nums = set(nums)

        for n in nums:
            if n - 1 in nums:
                continue
            
            count = 1
            while n + count in nums:
                count += 1
                res = max(res, count)
                
        
        return res

