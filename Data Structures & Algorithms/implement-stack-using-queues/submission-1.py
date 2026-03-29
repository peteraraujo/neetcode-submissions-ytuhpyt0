from collections import deque
class MyStack:

   

    def __init__(self):
        self.q = deque()

    def update(self):
        n = len(self.q) - 1
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def push(self, x: int) -> None:
        self.q.append(x)
        self.update()
        

    def pop(self) -> int:
        print(self.q)
        value = self.q.popleft()
        #self.update()
        return value
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()