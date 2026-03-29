class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        

        print(matrix)

        matrix.reverse()
        print(matrix)

        for y in range(len(matrix)):
            for x in range(y + 1, len(matrix)):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]

