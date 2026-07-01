class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ysize, xsize = m, n

        cache = [1] * xsize

        for _ in range(ysize - 1):
            for x in range(1, xsize):
                cache[x] = cache[x] + cache[x - 1]
        

        return cache[-1]