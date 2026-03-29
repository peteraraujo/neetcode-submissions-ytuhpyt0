class Solution:
    def tribonacci(self, n: int) -> int:
        if not n:
            return 0
        if n < 3:
            return 1
        
        p3, p2, p1 = 0, 1, 1

        for _ in range(2, n):
            p3, p2, p1 = p2, p1, p1+p2+p3
        return p1
