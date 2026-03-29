from collections import deque

class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 3:
            return n
        
        l1, l2 = 1, 2
        n -= 2

        for _ in range(n):
            l1, l2 = l2, l1 + l2
        
        return l2

        