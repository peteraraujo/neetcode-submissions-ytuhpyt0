class TreeNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        ySize, xSize = len(board), len(board[0])
        
        if not words:
            return []

        res = set()
        root = TreeNode()
        visited = set()

        # Add words to tree
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TreeNode()
                node = node.children[c]
            node.isEnd = True
        
        def dfs(y, x, substring, node):

            if y < 0 or x < 0 or y >= ySize or x >= xSize or (y, x) in visited or board[y][x] not in node.children:
                return
            
            visited.add((y, x))

            # Move to node with current char
            c = board[y][x]
            chilldNode = node.children[c]

            substring = substring + c

            if chilldNode.isEnd:
                res.add(substring)

            dfs(y, x + 1, substring, chilldNode)
            dfs(y, x - 1, substring, chilldNode)
            dfs(y + 1, x, substring, chilldNode)
            dfs(y - 1, x, substring, chilldNode)

            visited.remove((y, x))


        for y in range(len(board)):
            for x in range(len(board[0])):
                dfs(y, x, "", root)
                
        return list(res)

