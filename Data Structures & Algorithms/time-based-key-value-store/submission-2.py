from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list) # key: [ (time, value) ]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]

        if not arr:
            return ""
        
        size = len(arr)
        l, r = 0, size - 1

        while l <= r:
            m = (l + r) // 2
            ts = arr[m][0]
            if ts == timestamp:
                return arr[m][1]
            if ts < timestamp:
                l = m + 1
            else:
                r = m - 1
        
        return arr[l-1][1] if l != 0 else ""


        
