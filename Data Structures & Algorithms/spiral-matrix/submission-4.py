class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ysize, xsize = len(matrix), len(matrix[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        xsteps = xsize
        ysteps = ysize - 1

        y = 0
        x = -1
        res = []

        while (xsteps > 0 or ysteps > 0) and len(res) != (ysize * xsize):
            
            for yd, xd in dirs:
                xaxis = xd != 0

                for step in range(xsteps if xsteps and xaxis else ysteps):
                    y += yd
                    x += xd

                    res.append(matrix[y][x])
                
                if xaxis:
                    xsteps -= 1
                else:
                    ysteps -= 1

                if len(res) == (ysize * xsize):
                    break
        
        return res
