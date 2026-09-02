"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        visited = {}

        def dfs(currentNode):
            if currentNode.val in visited:
                return visited[currentNode.val]
            
            nei = []
            newNode = Node(currentNode.val, nei)
            visited[currentNode.val] = newNode

            for neighbor in currentNode.neighbors:
                nei.append(dfs(neighbor))

            
            
            return newNode
        
        return dfs(node)


        
        