class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        sizey, sizex = len(matrix), len(matrix[0])
        self.ps = [[0] *  (sizex + 1) for _ in range(sizey + 1)]
        for y in range(sizey):
            for x in range(sizex):
                self.ps[y + 1][x + 1] = matrix[y][x] + self.ps[y + 1][x + 1 - 1] + self.ps[y + 1 - 1][x + 1] - self.ps[y + 1 - 1][x + 1 - 1]

        

    def sumRegion(self, y1: int, x1: int, y2: int, x2: int) -> int:
        return self.ps[y2 + 1][x2 + 1] - self.ps[y1 + 1 - 1][x2 + 1] - self.ps[y2 + 1][x1 + 1 - 1] + self.ps[y1 + 1 - 1][x1 + 1 - 1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)