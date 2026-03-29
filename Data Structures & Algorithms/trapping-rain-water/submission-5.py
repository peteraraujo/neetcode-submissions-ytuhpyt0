class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)

        lmax = [0] * size
        rmax = [0] * size

        maxx = 0
        for i in range(size):
            maxx = max(maxx, height[i])
            lmax[i] = maxx
        
        maxx = 0
        for i in range(size - 1, -1, -1):
            maxx = max(maxx, height[i])
            rmax[i] = maxx
        
        tw = 0
        print(lmax, rmax)
        for i in range(size):
            tw += min(lmax[i], rmax[i]) - height[i]
        
        return tw



