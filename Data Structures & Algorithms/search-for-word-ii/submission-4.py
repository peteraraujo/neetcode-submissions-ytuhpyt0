class Node:
    def __init__(self):
        self.children = {} # char : Node
        self.end = ""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        sizey, sizex = len(board), len(board[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        root = Node()
        res = set()

        visited = set() # (y, x)
        

        for w in words:
            cur = root
            for char in w:
                if char not in cur.children:
                    cur.children[char] = Node()
                
                cur = cur.children[char]
            cur.end = w


        def search(y, x, node):
            if not (0 <= y < sizey) or not (0 <= x < sizex) or (y, x) in visited or board[y][x] not in node.children:
                return
            
            visited.add((y, x))
            

            node = node.children[board[y][x]]

            if node.end:
                res.add(node.end)
            
            for dy, dx in dirs:
                search(y + dy, x + dx, node)
            
            visited.remove((y, x))
        
        for y in range(sizey):
            for x in range(sizex):
                search(y, x, root)
        
        return list(res)
            

                
            
            
            
            





        
