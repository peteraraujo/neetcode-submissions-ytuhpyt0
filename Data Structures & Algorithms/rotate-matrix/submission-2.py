class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        sizey, sizex = len(matrix), len(matrix[0])

        for y in range(sizey):
            for x in range(y + 1, sizex):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
            matrix[y].reverse()