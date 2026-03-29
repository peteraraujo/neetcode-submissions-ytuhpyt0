import math
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = (l + r) // 2
            sq = m * m
            if sq == x:
                return m
            if sq < x:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res        
            




            

        
