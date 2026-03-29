class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        res = 0

        for l in range(len(heights) - 1):

            for r in range(len(heights) - 1, l, -1):
                width = r - l
                height = min(heights[l], heights[r])

                res = max(res, width * height)
        
        return res





