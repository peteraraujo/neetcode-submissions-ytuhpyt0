class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)

        def check(l, r):
            res = 0

            while l >= 0 and r < size:
                cl, cr = s[l], s[r]

                if cl == cr:
                    res += 1
                else:
                    break
                
                l -= 1
                r += 1
            
            return res
        
        res = 0

        for i in range(size):
            res += check(i, i)
        for i in range(size - 1):
            res += check(i, i + 1)
        
        return res