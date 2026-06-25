class Solution:
    def rob(self, nums: List[int]) -> int:
        p1 = p2 = 0

        for n in nums:
            p2, p1 = p1, max(n + p2, p1)
        
        return max(p1, p2)