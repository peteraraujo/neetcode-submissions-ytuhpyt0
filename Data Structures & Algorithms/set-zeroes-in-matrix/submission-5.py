class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ysize, xsize = len(matrix), len(matrix[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        for y in range(ysize):
            for x in range(xsize):
                matrix[y][x] = "m" if matrix[y][x] == 0 else matrix[y][x]
        
        for yz in range(ysize):
            for xz in range(xsize):
                if matrix[yz][xz] == "m":
                    matrix[yz][xz] = 0
                    for yd, xd in dirs:
                        y = yz
                        x = xz

                        while 0 <= y < ysize and 0 <= x < xsize:
                            if matrix[y][x] != "m":
                                matrix[y][x] = 0

                            y += yd
                            x += xd
