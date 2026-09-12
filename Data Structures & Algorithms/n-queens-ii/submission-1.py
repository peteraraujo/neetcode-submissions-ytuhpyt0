class Solution:
    def totalNQueens(self, n: int) -> int:
        dirs = ((1, 0), (1, -1), (1, 1))
        
        res = 0
        cs = Counter()

        def update(change, y, x):

            for yd, xd in dirs:
                cy, cx = y + yd, x + xd

                while (0 <= cy < n) and (0 <= cx < n):
                    
                    cs[(cy, cx)] += change

                    cy, cx = cy + yd, cx + xd


        def dfs(y):
            if y == n:
                nonlocal res
                res += 1
                return
            
            for x in range(n):
                if cs[(y, x)] > 0:
                    continue
                
                update(1, y, x)
                dfs(y + 1)
                update(-1, y, x)
        
        dfs(0)

        return res
