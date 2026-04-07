class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)

        res = 0

        def count(l, r):
            temp = 0

            while l >= 0 and r < size and s[l] == s[r]:
                temp += 1
                l -= 1
                r += 1
            
            return temp

        
        for i in range(size):
            
            res += count(i, i)
            res += count(i - 1, i)

        return res   


            




