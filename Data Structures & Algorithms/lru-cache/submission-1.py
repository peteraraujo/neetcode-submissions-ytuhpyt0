class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.count = 0

        self.nodes = {}
        self.head = None
        self.tail = None
        


    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        
        n = self.nodes[key]
        self.moveToTail(n)

        return n.value
    

    def addNode(self, n):
        if not self.head:
            self.head = self.tail = n
            return
        
        self.tail.next = n
        n.prev = self.tail
        self.tail = n
    
    def popHead(self):        
        if self.head is self.tail:
            self.head = self.tail = None
            return
        
        self.head = self.head.next
        self.head.prev = None
    
    def moveToTail(self, n):
        if self.tail is n:
            return
        
        if self.head is n:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            n.next = None

        if n.prev:
            n.prev.next = n.next
        
        if n.next:
            n.next.prev = n.prev

        n.prev = self.tail
        n.next = None

        self.tail.next = n
        self.tail = n
        
        

    def put(self, key: int, value: int) -> None:
        
        if key not in self.nodes and self.count == self.cap:
            self.nodes.pop(self.head.key)
            self.popHead()
            self.count -= 1
            
        
        if key not in self.nodes:
            n = Node(key, value)
            self.addNode(n)
            self.nodes[key] = n
            self.count += 1
        else:
            n = self.nodes[key]
            n.value = value
            self.moveToTail(n)






        
