class Solution:
    def scoreOfString(self, s: str) -> int:
        
        res = 0
        
        prev = s[0]
        for i in range(1, len(s)):
            c = s[i]
            res += abs(ord(prev) - ord(c))
            prev = c
        
        return res