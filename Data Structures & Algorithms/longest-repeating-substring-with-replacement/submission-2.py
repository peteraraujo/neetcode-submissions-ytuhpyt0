from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = len(s)
        l = 0
        maxw = 0 
        cs = Counter()

        for r in range(size):
            cs[s[r]] += 1
            mc = cs.most_common(1)
            mc = 0 if not mc else mc[0][1]
            while r - l + 1 - mc > k:
                cs[s[l]] -= 1
                l += 1
            maxw = max(maxw, r - l + 1)
        
        return maxw
