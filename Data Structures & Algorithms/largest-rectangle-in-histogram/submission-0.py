class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)

        res = 0
        stack = [] # (level, index)



        for i in range(size):
            index = i
            level = heights[i]



            while stack and level < stack[-1][0]:

                poppedlvl, poppedindex = stack.pop()
                index = poppedindex

                area = (i - poppedindex) * poppedlvl

                res = max(res, area)
                
            
            stack.append((level, index))

        for level, index in stack:
            area = (size - index) * level
            res = max(res, area)
        
        return res


            