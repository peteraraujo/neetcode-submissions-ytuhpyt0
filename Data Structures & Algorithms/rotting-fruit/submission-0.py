class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ySize, xSize = len(grid), len(grid[0])

        visited = set()
        queue = deque()

        fruitCount = 0

        for y in range(ySize):
            for x in range(xSize):
                if grid[y][x] == 2:
                    fruitCount += 1
                    visited.add((y, x))
                    queue.append((y, x))
                elif grid[y][x] == 1:
                    fruitCount += 1

        def addCell(y, x):
            if y < 0 or x < 0 or y >= ySize or x >= xSize or (y, x) in visited or grid[y][x] != 1:
                return False
            
            queue.append((y, x))
            visited.add((y, x))
        
        minute = 0

        while queue:
            for _ in range(len(queue)):
                fruitCount -= 1
                y, x = queue.popleft()
                addCell(y, x + 1)
                addCell(y, x - 1)
                addCell(y + 1, x)
                addCell(y - 1, x)
            
            if queue:
                minute += 1

        if fruitCount:
            return -1
        else:
            return minute
        
        
