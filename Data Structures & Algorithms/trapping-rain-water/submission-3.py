class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)

        maxsize = max(height)
        res = 0

        for h in range(1, maxsize + 1):
            wall = None
            for cell in range(0, size):
                iswall = h <= height[cell]

                if wall == None and not iswall:
                    continue

                if iswall and wall == None:
                    wall = cell
                    continue
                
                if iswall:
                    
                    res += max(0, ((cell - wall) + 1) - 2)
                    wall = cell
                    
        
        return res
                

                    
