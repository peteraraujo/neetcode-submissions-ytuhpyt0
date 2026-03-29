class MyCircularQueue:

    def __init__(self, k: int):
        self.count = 0
        self.cap = k

        self.array = [0] * k
        self.head, self.tail = 0, -1
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.count += 1
        self.tail = (self.tail + 1) % self.cap
        self.array[self.tail] = value
        
        return True
    

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.count -= 1
        self.head = (self.head + 1) % self.cap
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.tail]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.cap
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()