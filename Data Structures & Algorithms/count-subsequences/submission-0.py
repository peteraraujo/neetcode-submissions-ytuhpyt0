class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ssize = len(s)
        tsize = len(t)

        cache = {} # (si, ti) : count
        
        def dfs(si=0, ti=0):

            if ti == tsize:
                return 1

            if si == ssize:
                return 0

            query = (si, ti)

            if query in cache:
                return cache[query]
            
            schar, tchar = s[si], t[ti]
            
            take =  dfs(si + 1, ti + 1) if schar == tchar else 0
            
            skip = dfs(si + 1, ti)

            res = take + skip

            cache[query] = res

            return res
        
        return dfs()
        

            