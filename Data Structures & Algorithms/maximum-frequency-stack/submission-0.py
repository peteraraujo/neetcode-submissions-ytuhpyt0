from collections import Counter, OrderedDict
class FreqStack:

    def __init__(self):
        self.cs = Counter()
        self.stack = OrderedDict()
        self.count = 0

    def push(self, val: int) -> None:
        self.cs[val] += 1
        self.stack[(val, self.cs[val])] = self.count
        self.count += 1
        

    def pop(self) -> int:
        modes = self.cs.most_common()
        maxfreq = modes[0][1]
        
        modes = list(filter(lambda x: x[1] == maxfreq, list(modes)))
        
        toppest = modes[0][0] # (value, value count)
        toppestIndex = -1

        print(self.stack)
        print(maxfreq, self.cs)
        print(modes)
        for m in modes:
            value, c = m

            globalcount = self.stack[(value, c)]
            if globalcount > toppestIndex:
                toppestIndex = globalcount
                toppest = value
        
        print(toppest, maxfreq)
        self.cs[toppest] -= 1
        respop = self.stack.pop((toppest, maxfreq))

        print(respop)

        return toppest
        


       


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()