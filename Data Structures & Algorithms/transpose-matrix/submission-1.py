class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [ [ matrix[y][x] for y in range(len(matrix)) ] for x in range(len(matrix[0]))  ]