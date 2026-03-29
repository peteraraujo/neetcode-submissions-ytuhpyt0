class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        d = [0] * 26

        base = ord("a")

        for c in s:
            d[ord(c) - base] += 1
        
        for c in t:
            d[ord(c) - base] -= 1
            if d[ord(c) - base] < 0:
                return False

        return True


