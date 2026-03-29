class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ySize = len(matrix)
        xSize = len(matrix[0])

        def spreadH(x):
            for y in range(ySize):
                if matrix[y][x] != "FLAG":
                    matrix[y][x] = 0
        
        def spreadV(y):
            for x in range(xSize):
                if matrix[y][x] != "FLAG":
                    matrix[y][x] = 0

        for y in range(ySize):
            for x in range(xSize):
                if matrix[y][x] == 0:
                    matrix[y][x] = "FLAG"
        
        for y in range(ySize):
            for x in range(xSize):
                if matrix[y][x] == "FLAG":
                    matrix[y][x] = 0
                    spreadH(x)
                    spreadV(y)
        

        
        

        
        










