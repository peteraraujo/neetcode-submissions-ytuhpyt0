class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ySize, xSize = len(board), len(board[0])
        
        invalid = set()
        

        def dfs(y, x):
            if y < 0 or x < 0 or y >= ySize or x >= xSize or board[y][x] == "X" or (y, x) in invalid:
                return
            
            invalid.add((y, x))

            dfs(y + 1, x)
            dfs(y - 1, x)
            dfs(y, x + 1)
            dfs(y, x - 1)


        for x in range(xSize):
            if board[0][x] == "O" and (0, x) not in invalid:
                dfs(0, x)
            if board[ySize - 1][x] == "O" and (ySize - 1, x) not in invalid:
                dfs(ySize - 1, x)
        
        for y in range(ySize):
            if board[y][0] == "O" and (y, 0) not in invalid:
                dfs(y, 0)
            if board[y][xSize - 1] == "O" and (y, xSize - 1) not in invalid:
                dfs(y, xSize - 1)
        

        for y in range(1, ySize - 1):
            for x in range(1, xSize - 1):
                if board[y][x] == "O" and (y, x) not in invalid:
                    board[y][x] = "X"
        