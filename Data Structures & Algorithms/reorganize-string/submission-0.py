import heapq as h
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        cs = Counter(s)
        mh = list(map(lambda x: [-x[1], x[0]], cs.items()))
        h.heapify(mh)

        res = []

        for _ in range(len(s)):
            if not res or res[-1] != mh[0][1]:
                last = h.heappop(mh)
                last[0] += 1
                res.append(last[1])
                if last[0] != 0:
                    h.heappush(mh, last)
                continue
            
            last = h.heappop(mh)
            if not mh:
                return ""
            last2 = h.heappop(mh)
            h.heappush(mh, last)
            last2[0] += 1
            res.append(last2[1])
            if last2[0] != 0:
                h.heappush(mh, last2)
        
        return "".join(res)
        
            
        







