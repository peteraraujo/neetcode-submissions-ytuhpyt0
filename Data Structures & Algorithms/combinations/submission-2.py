class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [ [i] for i in range(1, n + 1)]

        res = []

        cache = []
        for e in range(1, n + 1):
            temp = [[e]]
            for saved in cache:
                new = saved[:]
                new.append(e)

                if len(new) >= k:
                    res.append(new)
            
                else:
                    temp.append(new)
            
            cache.extend(temp)
        
        
        return res




        