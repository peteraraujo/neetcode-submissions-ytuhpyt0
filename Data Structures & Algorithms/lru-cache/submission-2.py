from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodes = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        self.nodes.move_to_end(key, last=True)
        return self.nodes[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes and len(self.nodes) == self.cap:
            self.nodes.popitem(last=False)
        
        self.nodes[key] = value
        self.nodes.move_to_end(key, last=True)