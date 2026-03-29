class UF:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0
    
    def findParent(self, node):
        cur = node
        while self.parent[cur] != cur:
            
            # Path Compression
            self.parent[cur] = self.parent[self.parent[cur]]

            cur = self.parent[cur]
        
        return cur
    
    def union(self, a, b):
        p1, p2 = self.findParent(a), self.findParent(b)

        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        
        return True


                   



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges)
        
        uf = UF(size)

        for a, b in edges:
            if not uf.union(a, b):
                return [a, b]
                

























