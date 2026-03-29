class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0

        # area = (r - l) * min(height)
        l, r = 0, size - 1
        while l < r:
            res = max(res, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
        



