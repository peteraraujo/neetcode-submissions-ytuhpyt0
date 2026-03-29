from collections import OrderedDict, Counter

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.items = OrderedDict()
        self.cs = Counter()
        

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        
        self.items.move_to_end(key, last=True)
        self.cs[key] += 1

        return self.items[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.items and len(self.items) == self.cap:
            
            lfus = self.cs.most_common()[::-1]
            minfreq = lfus[0][1]
            lfus = list(filter(lambda x: x[1] == minfreq, lfus))

            if len(lfus) == 1:
                self.cs.pop(lfus[0][0])
                self.items.pop(lfus[0][0])

            else:
                self.cs.pop(self.items.popitem(last=False)[0])

                
        

        self.cs[key] += 1
        self.items[key] = value
        self.items.move_to_end(key, last=True)





        
        





        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)