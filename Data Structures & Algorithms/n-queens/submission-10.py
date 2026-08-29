class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        QUEEN, EMPTY = 'Q', '.'
        board = [[EMPTY] * n for _ in range(n)]
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

        cs = Counter()

        res = []

        median = n // 2

        def update(occupy, yo, xo):

            for yd, xd in dirs:
                y, x = yo + yd, xo + xd

                while (0 <= y < n) and (0 <= x < n):
                    cs[(y, x)] += 1 if occupy else -1

                    y += yd
                    x += xd
        
        def dfs(y=1, unique=False):
            if y == n:
                res.append(["".join(row) for row in board])
                

                if unique:
                    return

                res.append(["".join(reversed(row)) for row in board])
                return
            
            for x in range(n):
                if cs[(y, x)] > 0:
                    continue
                
                update(True, y, x)
                board[y][x] = QUEEN
                dfs(y + 1, unique)
                update(False, y, x)
                board[y][x] = EMPTY

        
        for x in range(math.ceil(n / 2)):
            update(True, 0, x)
            board[0][x] = QUEEN
            dfs(1, x == median)
            update(False, 0, x)
            board[0][x] = EMPTY

        return res
