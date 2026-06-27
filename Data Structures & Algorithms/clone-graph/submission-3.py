"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        nodes = {} # value, node

        def dfs(n):
            
            if n.val in nodes:
                return nodes[n.val]

            current = Node(n.val)
            nodes[n.val] = current

            for nei in n.neighbors:
                current.neighbors.append(dfs(nei))
            
            return current
        
        return dfs(node) if node else None

                

            