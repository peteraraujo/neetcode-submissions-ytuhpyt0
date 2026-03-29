class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        sizey, sizex = len(text1) + 1, len(text2) + 1

        cache = [ [0] * (sizex) for _ in range(sizey) ]
        
        res = 0

        for y in range(1, sizey):
            for x in range(1, sizex):
                if text1[y - 1] == text2[x - 1]:
                    cache[y][x] = cache[y - 1][x - 1] + 1
                else:
                    cache[y][x] = max(cache[y - 1][x], cache[y][x - 1])

        return cache[-1][-1]