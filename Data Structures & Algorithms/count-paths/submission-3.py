class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ysize, xsize = m, n

        t = [1] * xsize
        b = [1] * xsize

        for _ in range(ysize - 1):
            for x in range(1, xsize):
                b[x] = b[x - 1] + t[x]

            t, b = b, [1] * xsize
        

        return t[-1]