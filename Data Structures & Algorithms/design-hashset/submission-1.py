class MyHashSet:

    def __init__(self):
        self.l = [[] for _ in range(100)]
        

    def add(self, key: int) -> None:
        if key not in self.l[key % 100]:
            self.l[key % 100].append(key)
        

    def remove(self, key: int) -> None:
        if key in self.l[key % 100]:
            self.l[key % 100].pop(self.l[key % 100].index(key))
        

    def contains(self, key: int) -> bool:
        return key in self.l[key % 100]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)