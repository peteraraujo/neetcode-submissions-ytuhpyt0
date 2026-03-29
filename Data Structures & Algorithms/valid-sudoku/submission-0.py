class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        size = len(board)

        boxes = [[set() for _ in range(len(board[0]) // 3) ] for _ in range(len(board) // 3)]

        rows = [set() for _ in range(size)]
        cols = [set() for _ in range(size)]

        for y in range(size):
            for x in range(size):
                n = board[y][x]

                if n == ".":
                    continue

                if (n in rows[y]) or (n in cols[x]) or (n in boxes[y // 3][x // 3]):
                    return False
                rows[y].add(n)
                cols[x].add(n)
                boxes[y // 3][x // 3].add(n)

                print(f"{rows=}")
                print(f"{cols=}")
                print(f"{boxes=}")
        
        return True


