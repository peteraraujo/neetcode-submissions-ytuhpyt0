class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ySize, xSize = len(board), len(board[0])
        visited = set()

        def dfs(y, x, i):
            if i == len(word):
                return True
            
            if (x < 0 or y < 0 or x >= xSize or y >= ySize 
             or word[i] != board[y][x] or (y, x) in visited):
                return False
            
            visited.add((y, x))

            res = (
                dfs(y + 1, x, i + 1) or 
                dfs(y - 1, x, i + 1) or
                dfs(y, x + 1, i + 1) or
                dfs(y, x - 1, i + 1)
            )

            visited.remove((y, x))

            return res

        for y in range(ySize):
            for x in range(xSize):
                if dfs(y, x, 0): return True
        
        return False








