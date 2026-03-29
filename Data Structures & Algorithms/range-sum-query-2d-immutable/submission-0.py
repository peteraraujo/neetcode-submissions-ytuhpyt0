class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        sizey, sizex = len(matrix), len(matrix[0])
        self.matrix = [[0] * (sizex + 1) for _ in range(sizey + 1) ]

        for y in range(sizey):
            for x in range(sizex):
                self.matrix[y+1][x+1] = matrix[y][x] + self.matrix[y+1][x+1-1] + self.matrix[y+1-1][x+1] - self.matrix[y+1-1][x+1-1]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2+1][col2+1] - self.matrix[row2+1][col1+1-1] - self.matrix[row1+1-1][col2+1] + self.matrix[row1+1-1][col1+1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)