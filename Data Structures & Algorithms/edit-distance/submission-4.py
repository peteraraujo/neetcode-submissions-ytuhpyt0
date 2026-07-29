from heapq import heappush, heappop

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ops = {
            "k": (0, 1, 1),
            "d": (1, 1, 0),
            "i": (1, 0, 1),
            "r": (1, 1, 1),
        }

        def update(query, op):
            opd = ops[op]
            return (query[0] + opd[0], query[1] + opd[1], query[2] + opd[2])
        

        size1, size2 = len(word1), len(word2)

        cache = set() 
        hq = [(0, 0, 0)]

        res = float("inf")
        
        while hq:
            
            query = heappop(hq)

            if query in cache:
                continue

            op, i1, i2 = query

            # Both got to the end
            if i1 == size1 and i2 == size2:
                res = min(res, op)
                continue
            
            # Only w1 got to the end. Insert the rest from w2
            if i1 == size1:
                res = min(res, op + size2 - i2)
                continue
            
            # Only w2 got to the end. Delete the extra characters from w1
            if i2 == size2:
                res = min(res, op + size1 - i1)
                continue


            w1, w2 = word1[i1], word2[i2]

            if w1 == w2:
                heappush(hq, update(query, "k"))
                continue

            heappush(hq, update(query, "d"))
            heappush(hq, update(query, "i")) 
            heappush(hq, update(query, "r"))

            cache.add(query)    
        
        return res

            

    

