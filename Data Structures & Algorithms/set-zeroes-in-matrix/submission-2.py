class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ySize = len(matrix)
        xSize = len(matrix[0])

        cols = set()
        rows = set()

        for y in range(ySize):
            for x in range(xSize):
                if (val := matrix[y][x]) == 0:
                    cols.add(x)
                    rows.add(y)
        
        for y in range(ySize):
            if y in rows:
                matrix[y][:] = [0] * xSize
                continue
            
            for x in range(xSize):
                if x in cols:
                    matrix[y][x] = 0
        
        










