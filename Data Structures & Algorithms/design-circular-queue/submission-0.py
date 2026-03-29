class Node:
    def __init__(self, v, n=None):
        self.v = v
        self.next = n

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.count = 0

        self.head = None
        self.tail = None
        


    def enQueue(self, value: int) -> bool:

        if self.count >= self.cap:
            return False

        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.count += 1
        return True
        

    def deQueue(self) -> bool:
        if not self.head:
            return False
        
        node = self.head
        self.head = self.head.next

        if not self.head:
            self.tail = None
        
        self.count -= 1
        return True
        

    def Front(self) -> int:
        return self.head.v if self.head else -1

    def Rear(self) -> int:
        return self.tail.v if self.tail else -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.cap



# exit <- item item item <- entry

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()