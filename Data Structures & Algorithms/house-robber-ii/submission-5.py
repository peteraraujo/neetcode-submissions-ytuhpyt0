class Solution:
    def rob(self, nums: List[int]) -> int:

        size = len(nums)

        if size == 1:
            return nums[0]
        
        def run(start, end):
            p2 = p1 = 0
            for i in range(start, end):
                n = nums[i]
                p2, p1 = p1, max(n + p2, p1)
            
            return max(p1, p2)
        
        return max(run(0, size - 1), run(1, size))