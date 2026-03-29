class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        yLength = len(matrix)
        xLength = len(matrix[0])

        left = 0
        right = xLength - 1


        top = 0
        bottom = yLength - 1

        while top <= bottom and left <= right:
            for x in range(left, right + 1):
                res.append(matrix[top][x])

            top += 1

            for y in range(top, bottom + 1):
                res.append(matrix[y][right])

            right -= 1

            if top <= bottom:
                for x in range(right, left - 1, -1):
                    res.append(matrix[bottom][x])

                bottom -= 1

            if left <= right:
                for y in range(bottom, top - 1, -1):
                    res.append(matrix[y][left])

                left += 1

        return res