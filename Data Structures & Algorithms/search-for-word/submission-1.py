class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowSize, colSize = len(board), len(board[0])

        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if c < 0 or r < 0 or c >= colSize or r >= rowSize or (r, c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r, c))

            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1)

            visited.remove((r, c))

            return res
        
        for r in range(rowSize):
            for c in range(colSize):
                if dfs(r, c, 0): return True
        
        return False

