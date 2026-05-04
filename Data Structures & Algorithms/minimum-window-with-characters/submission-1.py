from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        size = len(s)
        res = s
        
        tc = defaultdict(int)
        wc = defaultdict(int)

        for c in t:
            tc[c] += 1
        

        def compare():
            for k in tc:
                if k not in wc or wc[k] < tc[k]:
                    return False
            return True

        l = 0

        for r in range(size):
            c = s[r]
            wc[c] += 1

            if compare():
                # Here!
                while l <= r and (s[l] not in tc or wc[s[l]] > tc[s[l]]):
                    wc[s[l]] -= 1
                    l += 1
                
                if len(s[l:r + 1]) < len(res):
                    res = s[l:r + 1]
        
        return res if compare() else ""
                
            

