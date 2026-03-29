class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ysize, xsize = len(image), len(image[0])

        old = image[sr][sc]
        visited = set()
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def paint(y, x):
            if y < 0 or y >= ysize or x < 0 or x >= xsize or (y, x) in visited or image[y][x] != old:
                return
            
            visited.add((y, x))

            image[y][x] = color

            for yd, xd in dirs:
                paint(y + yd, x + xd)
        
        paint(sr, sc)

        return image

            
            
