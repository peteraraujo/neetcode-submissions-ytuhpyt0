class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ysize, xsize = len(matrix), len(matrix[0])

        for y in range(ysize):
            for x in range(y, xsize):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
            
            matrix[y].reverse()
        
        