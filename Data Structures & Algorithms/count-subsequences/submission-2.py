class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ssize = len(s)
        tsize = len(t)

        cache = [[0] * (ssize + 1) for _ in range(tsize + 1)]
        cache[0] = [1] * (ssize + 1)

        for ti in range(tsize):
            for si in range(ssize):
                cti, csi = ti + 1, si + 1

                tchar, schar = t[ti], s[si]

                take = cache[cti - 1][csi - 1] if tchar == schar else 0
                skip = cache[cti][csi - 1]

                cache[cti][csi] = take + skip
        
        return cache[-1][-1]
                
