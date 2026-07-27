class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        size1 = len(s1)
        size2 = len(s2)
        size3 = len(s3)

        if size1 + size2 != size3:
            return False

        cache = set() # (s1, s2)

        def dfs(i1=0, i2=0, i3=0):

            query = (i1, i2, i3)

            if i3 == size3:
                return True
            
            if query in cache:
                return False
            
            next1 = s1[i1] if i1 < size1 else None
            next2 = s2[i2] if i2 < size2 else None
            next3 = s3[i3]

            if next1 and next1 == next3:
                pick1 = dfs(i1 + 1, i2, i3 + 1)

                if pick1:
                    return True
            
            if next2 and next2 == next3:
                pick2 = dfs(i1, i2 + 1, i3 + 1)
            
                if pick2:
                    return True

            cache.add(query)

            return False
        
        return dfs()
            
