class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ysize, xsize = len(matrix), len(matrix[0])

        coords = set() # (y, x)
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1)) 

        for y in range(ysize):
            for x in range(xsize):
                if matrix[y][x] == 0:
                    coords.add((y, x))
        
        for yz, xz in coords:
            for yd, xd in dirs:
                y = yz
                x = xz

                while 0 <= y < ysize and 0 <= x < xsize:
                    matrix[y][x] = 0
                    y += yd
                    x += xd
        
