class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ysize, xsize = len(matrix), len(matrix[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        cache = [[-1] * xsize for y in range(ysize)]

        def dfs(y, x, prev, visiting):
            query = (y, x)

            if not (0 <= y < ysize) or not (0 <= x < xsize) or matrix[y][x] <= prev or query in visiting:
                return 0
            
            visiting.add(query)

            if cache[y][x] != -1:
                return cache[y][x]
            
            res = 0

            for yd, xd in dirs:
                res = max(res, dfs(y + yd, x + xd, matrix[y][x], visiting))
            
            res += 1

            cache[y][x] = res
            
            visiting.remove(query)
            return res
            

            


        res = 0

        for y in range(ysize):
            for x in range(xsize):
                res = max(res, dfs(y, x, -1, set()))
        
        for c in cache:
            print(c)

        return res
                


                