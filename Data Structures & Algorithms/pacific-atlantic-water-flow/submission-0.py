class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ySize, xSize = len(heights), len(heights[0])

        pac, atl = set(), set()
        res = []

        def dfs(y, x, visited, prevHeight):
            if (y, x) in visited or y < 0 or x < 0 or y >= ySize or x >= xSize or heights[y][x] < prevHeight:
                return
            
            visited.add((y, x))
            dfs(y + 1, x, visited, heights[y][x])
            dfs(y - 1, x, visited, heights[y][x])
            dfs(y, x + 1, visited, heights[y][x])
            dfs(y, x - 1, visited, heights[y][x])
        
        for x in range(xSize):
            dfs(0, x, pac, heights[0][x])
            dfs(ySize - 1, x, atl, heights[ySize - 1][x])
        
        for y in range(ySize):
            dfs(y, 0, pac, heights[y][0])
            dfs(y, xSize - 1, atl, heights[y][xSize - 1])

        for y in range(ySize):
            for x in range(xSize):
                if (y, x) in pac and (y, x) in atl:
                    res.append([y, x])
        
        return res

