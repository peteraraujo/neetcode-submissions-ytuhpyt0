import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        

        while l <= r:
            m = (l + r) // 2

            res = 0

            for p in piles:
                res += math.ceil(p / m)
            
            print(f"{l=} | {r=} | {m=} | {res=}")

            if res > h:
                l = m + 1
            else:
                r = m - 1
        
        return r + 1
        
            
            

