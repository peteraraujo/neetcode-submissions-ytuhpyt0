class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sizey, sizex = len(matrix), len(matrix[0])

        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        steps = [sizex, sizey - 1]
        y = 0
        x = -1
        d = 0

        res = []

        while sc := steps[d % 2]:
            for _ in range(sc):
                y += dirs[d][0]
                x += dirs[d][1]
                res.append(matrix[y][x])
            
            steps[d % 2] -= 1
            d = (d + 1) % 4
        
        return res
            
            



