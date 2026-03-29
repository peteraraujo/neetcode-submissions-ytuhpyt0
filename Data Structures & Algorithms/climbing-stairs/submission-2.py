class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        pre, current = 2, 3

        for _ in range(4, n + 1):
            pre, current = current, pre + current
        
        return current