class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ssize = len(s)
        tsize = len(t)

        prevRow = [1] * (ssize + 1)

        for ti in range(tsize):

            row = [0] * (ssize + 1)
            
            for si in range(ssize):
                srowi = si + 1

                tchar, schar = t[ti], s[si]

                take = prevRow[srowi - 1] if tchar == schar else 0
                skip = row[srowi - 1]

                row[srowi] = take + skip
            
            prevRow = row
        
        return prevRow[-1]



                

        
        