class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        size = len(matrix)

        # Transposition
        for y in range(size):
            for x in range(y + 1, size):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]

            matrix[y].reverse()
        


