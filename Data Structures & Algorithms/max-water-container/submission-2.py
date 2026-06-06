class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)

        l = 0
        r = size - 1

        gMax = 0

        while l < r:
            dist = r - l
            cap = dist * min(heights[l], heights[r])

            gMax = max(gMax, cap)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return gMax