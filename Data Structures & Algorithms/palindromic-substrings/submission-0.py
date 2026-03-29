class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0

        def countPal(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(len(s)):

            # Odd
            res += countPal(i, i)

            # Even
            res += countPal(i, i + 1)
        
        return res