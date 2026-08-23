class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sizey, sizex = len(matrix), len(matrix[0])

        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        hcount = sizex
        vcount = sizey - 1
        

        i = 0

        y, x = 0, -1

        res = []

        while vcount > 0 or hcount > 0:
            
            # Horizontal
            yd, xd = dirs[i]

            for _ in range(hcount):
                y += yd
                x += xd
                res.append(matrix[y][x])

            i = (i + 1) % len(dirs)
            hcount -= 1

            if vcount == 0:
                break


            # Vertical
            yd, xd = dirs[i]

            for _ in range(vcount): 
                y += yd
                x += xd
                res.append(matrix[y][x])

            i = (i + 1) % len(dirs)
            vcount -= 1

            if hcount == 0:
                break
        

        return res
