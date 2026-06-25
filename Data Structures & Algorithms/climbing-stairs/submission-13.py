class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        prev = 2
        prev2 = 1

        for step in range(3, n + 1):
            prev2, prev = prev, prev2 + prev
        
        return prev
