class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [ [0] * n for _ in range(n) ] # >= 0 -> counter ; -1 -> Queen

        res = []

        def update(y, x, yd, xd, change):
            while 0 <= y < n and 0 <= x < n:
                board[y][x] += change
                y += yd
                x += xd

        def move(y, x, change):
            # Horizontal
            update(y, 0, 0, 1, change)

            # Vertical
            update(0, x, 1, 0, change)

            # Diagonal
            # Up-Left
            update(y, x, -1, -1, change)

            # Down-Right
            update(y, x, 1, 1, change)

            # Antidiagonal
            # Up-Right
            update(y, x, -1, 1, change)

            # Down-Left
            update(y, x, 1, -1, change)

            # Place queen
            board[y][x] = -1 if change > 0 else 0
    

        def dfs(y):
            # Base cases
            if y == n:
                snapshot = [ [0] * n for _ in range(n) ]
                for y in range(n):
                    for x in range(n):
                        snapshot[y][x] = '.' if board[y][x] >= 0 else "Q"
                    snapshot[y] = "".join(snapshot[y])
                res.append(snapshot)
            
            # Traverse
            for x in range(n):
                if board[y][x] == 0:
                    move(y, x, 1)
                    dfs(y + 1)
                    move(y, x, -1)
        
        dfs(0)

        print(res)
        
        return res
