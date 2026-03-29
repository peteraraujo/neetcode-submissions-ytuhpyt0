class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ySize, xSize = len(grid), len(grid[0])

        visited = set()
        queue = deque()

        def addCell(y, x):
            if x < 0 or y < 0 or x >= xSize or y >= ySize or (y, x) in visited or grid[y][x] == -1:
                return
            
            visited.add((y, x))
            queue.append([y, x])

        for y in range(ySize):
            for x in range(xSize):
                if grid[y][x] == 0:
                    queue.append([y, x])
                    visited.add((y, x))
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                y, x = queue.popleft()
                grid[y][x] = dist
                addCell(y + 1, x)
                addCell(y - 1, x)
                addCell(y, x + 1)
                addCell(y, x - 1)
            dist += 1
