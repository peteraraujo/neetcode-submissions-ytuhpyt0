class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)] # y
        cols = [set() for _ in range(9)] # x
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for y in range(9):
            for x in range(9):
                if (n := board[y][x]) != ".":
                    # Check
                    if n in rows[y] or n in cols[x] or n in boxes[y//3][x//3]:
                        return False

                    # Add
                    rows[y].add(n)
                    cols[x].add(n)
                    boxes[y//3][x//3].add(n)
        
        return True


