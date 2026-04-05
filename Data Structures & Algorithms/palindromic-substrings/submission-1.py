class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        res = 0

        def pal(start, end):

            
            while start < end:
                if s[start] != s[end]:
                    return False

                start += 1
                end -= 1    
            
            return True

        
        for i in range(size):
            for j in range(i, size):
                if pal(i, j):
                    res += 1
        
        return res
                




        

            


