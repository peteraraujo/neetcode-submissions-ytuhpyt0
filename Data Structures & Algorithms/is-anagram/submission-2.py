class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        from collections import Counter

        c = Counter()

        for i in range(len(s)):
            c[s[i]] += 1
            c[t[i]] -= 1
        
        if c.most_common(1) and c.most_common(1)[0][1] != 0:
            return False
        
        return True


