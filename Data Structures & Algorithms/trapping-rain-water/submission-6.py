class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)

        res = 0

        pmax = [0] * size
        pmax[0] = height[0]
        for i in range(size):
            pmax[i] = max(pmax[i - 1], height[i])
        
        smax = [0] * size
        smax[-1] = height[-1]
        for i in range(size - 2, -1, -1):
            smax[i] = max(smax[i + 1], height[i])

        for i in range(size):
            res += min(pmax[i], smax[i]) - height[i]

        return res