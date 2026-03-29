class DS:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.count = n

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def findParent(self, node):
        cur = node

        while cur != self.parent[cur]:
            cur = self.parent[cur]

            # Path compression
            self.parent[cur] = self.parent[self.parent[cur]]
        
        return cur

    def union(self, a, b):
        pa, pb = self.findParent(a), self.findParent(b)

        if pa == pb:
            return False
        
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        else:
            self.parent[pa] = pb
            self.rank[pb] = pa
        

        self.count -= 1
        return True
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DS(n)
        
        for a, b in edges:
            ds.union(a, b)
        
        return ds.count







