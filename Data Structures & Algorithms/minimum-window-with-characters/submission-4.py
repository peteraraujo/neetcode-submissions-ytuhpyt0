from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size = len(s)

        res = ""
        
        tc = Counter(t)
        sc = Counter()

        l = 0
        
        for r in range(size):
            sc[s[r]] += 1
            
            while l < size and (sc[s[l]] - 1) >= tc[s[l]]:
                sc[s[l]] -= 1
                l += 1
            

            for char in tc:
                if sc[char] < tc[char]:
                    break
            else:
                res = s[l : r + 1] if not res or len(res) > (r - l) + 1 else res
            

        return res    

        







