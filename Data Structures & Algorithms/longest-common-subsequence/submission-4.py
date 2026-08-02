class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        size1 = len(text1)
        size2 = len(text2)

        cache = {} # (i1, i2) = length

        def dfs(i1=0, i2=0):
            query = (i1, i2)

            if query in cache:
                return cache[query]

            if i1 == size1 or i2 == size2:
                return 0
            
            c1, c2 = text1[i1], text2[i2]

            res = 0

            if c1 == c2:
                res += 1 + dfs(i1 + 1, i2 + 1)
            
            else:
                i1Path = dfs(i1 + 1, i2)
                i2Path = dfs(i1, i2 + 1)
                res = max(i1Path, i2Path)
            
            cache[query] = res

            return res
        

        return dfs()