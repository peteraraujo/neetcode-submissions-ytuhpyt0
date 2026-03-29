"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        res = []

        def dfs(n):
            if not n:
                return

            for c in n.children:
                dfs(c)

            res.append(n.val)
        
        dfs(root)
        return res