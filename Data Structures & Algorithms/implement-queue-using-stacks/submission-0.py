class MyQueue:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        temp = []
        for _ in range(len(self.s)):
            temp.append(self.s.pop())
        self.s.append(x)
        for _ in range(len(temp)):
            self.s.append(temp.pop())
        
        

    def pop(self) -> int:
        return self.s.pop()
        

    def peek(self) -> int:
        return self.s[-1]
        

    def empty(self) -> bool:
        return not self.s
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()