class CountSquares:

    totalCount = 1001

    def __init__(self):
        self.m = [ [0] * self.totalCount for _ in range(self.totalCount) ]

    def add(self, point: List[int]) -> None:
        x, y = point
        self.m[y][x] += 1
        

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for searchY in range(self.totalCount):
            if searchY == y:
                continue
            
            if (countY := self.m[searchY][x]) > 0:
                diff = searchY - y
                absDiff = abs(diff)

                # Search left
                searchX = x - absDiff
                if searchX >= 0:
                    if (countX := self.m[searchY][searchX]) > 0:
                        if (countJoin := self.m[y][searchX]) > 0:
                            # Square found
                            res += countJoin * countY * countX
                # Search right
                searchX = x + absDiff
                if searchX < len(self.m[0]):
                    if (countX := self.m[searchY][searchX]) > 0:
                        if (countJoin := self.m[y][searchX]) > 0:
                            # Square found
                            res += countJoin * countY * countX
        return res

 
