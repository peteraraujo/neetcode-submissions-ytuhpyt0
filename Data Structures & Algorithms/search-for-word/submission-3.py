class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        sizey, sizex, sizew = len(board), len(board[0]), len(word)
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        visited = set() # (y, x)

        def search(i, y, x):
            if i == sizew:
                return True
            
            if not (0 <= y < sizey) or not (0 <= x < sizex) or board[y][x] != word[i] or (y, x) in visited:
                return False
            
            visited.add((y, x))

            for yd, xd in dirs:
                if search(i + 1, y + yd, x + xd):
                    return True
            
            visited.remove((y, x))

            return False

        for y in range(sizey):
            for x in range(sizex):
                if search(0, y, x):
                    return True
        
        return False
            
            

