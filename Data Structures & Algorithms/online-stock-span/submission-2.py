class StockSpanner:

    def __init__(self):
        self.h = []
        

    def next(self, price: int) -> int:
        self.h.append(price)
        res = 0
        for i in range(len(self.h) - 1, -1, -1):
            if self.h[i] <= price:
                res += 1
                continue
            else:
                break

        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)