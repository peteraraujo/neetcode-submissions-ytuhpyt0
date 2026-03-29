class UnionFind:
    
    def __init__(self, n: int):
        self.count = n

        self.parent = {}
        self.height = {}

        for i in range(0, n):
            self.parent[i] = i
            self.height[i] = 0
        

    def find(self, x: int) -> int:
        cur = self.parent[x]

        while cur != self.parent[cur]:
            
            self.parent[cur] = self.parent[self.parent[cur]]

            cur = self.parent[cur]

        return cur
        

    def isSameComponent(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        return p1 == p2

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        
        if self.height[p1] > self.height[p2]:
            self.parent[p2] = p1
        elif self.height[p1] < self.height[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.height[p1] += 1
        
        self.count -= 1

        return True
        





    def getNumComponents(self) -> int:
        return self.count

