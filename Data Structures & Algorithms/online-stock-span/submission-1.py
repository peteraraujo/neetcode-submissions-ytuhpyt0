class StockSpanner:

    def __init__(self):
        self.h = []
        

    def next(self, price: int) -> int:
        self.h.append(price)
        temp = self.h.copy()
        res = 0
        while temp:
            if temp.pop() <= price:
                res += 1
                continue
            else:
                break
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)