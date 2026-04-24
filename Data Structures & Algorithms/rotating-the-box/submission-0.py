class Solution:
    def rotateTheBox(self, g: List[List[str]]) -> List[List[str]]:
        sizey, sizex = len(g), len(g[0])

        STONE = "#"
        OBS = "*"
        EMPTY = "."

        g = [ [ g[y][x] for y in range(sizey - 1, -1, -1)] for x in range(sizex)  ]

        sizey, sizex = len(g), len(g[0])

        for y in range(sizey - 1, -1 , -1):
            for x in range(sizex):
                cell = g[y][x]

                if cell == STONE:
                    
                    ny = y
                    while ny + 1 < sizey and g[ny + 1][x] == EMPTY:
                        
                        ny += 1
                    
                    g[y][x] = EMPTY
                    g[ny][x] = STONE
        
        return g


        