class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        size1 = len(text1)
        size2 = len(text2)

        cache = [[0] * (size2 + 1) for _ in range(size1 + 1)]

        for i1 in range(size1):
            for i2 in range(size2):
                
                char1, char2 = text1[i1], text2[i2]

                cy, cx = i1 + 1, i2 + 1

                if char1 == char2:
                    cache[cy][cx] = cache[cy - 1][cx - 1] + 1
                    continue
                
                cache[cy][cx] = max(cache[cy - 1][cx], cache[cy][cx - 1])
        
        return cache[-1][-1]
                




                
                

        