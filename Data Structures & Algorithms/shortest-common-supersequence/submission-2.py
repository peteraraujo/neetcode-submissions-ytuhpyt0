class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        size1, size2 = len(str1), len(str2)
        
        dp = [ [""] * (size2 + 1) for _ in range(size1 + 1) ]

        cur = []
        for y in range(size1):
            cur.append(str1[y])
            row = dp[y + 1][0] = "".join(cur)
        
        cur.clear()
        for x in range(size2):
            cur.append(str2[x])
            col = dp[0][x + 1] = "".join(cur)
        
        for i1 in range(size1):
            for i2 in range(size2):
                
                c1, c2 = i1 + 1, i2 + 1

                char1, char2 = str1[i1], str2[i2]

                if char1 == char2:
                    dp[c1][c2] = dp[c1 - 1][c2 - 1] + char1
                    continue

                path1 = dp[c1 - 1][c2] + char1
                path2 = dp[c1][c2 - 1] + char2

                dp[c1][c2] = path1 if len(path1) < len(path2) else path2
        
        return dp[-1][-1]



                


