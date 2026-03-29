class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        size = len(arr)

        gcount = 1
        cur = 1
        prev = arr[0]
        state = 0 # 0 = None ; 1 = Prev2 > Prev1 ; 2 = Prev2 < Prev1 

        for i in range(1, size):
            n = arr[i]

            if n == prev:
                state = 0
                cur = 1
            
            elif state == 0:
                state = 1 if prev > n else 2
                cur += 1
            
            elif (state == 1 and prev < n) or (state == 2 and prev > n):
                cur += 1
                state = 1 if prev > n else 2
            
            else:
                state = 1 if prev > n else 2
                cur = 2

            prev = n
            gcount = max(gcount, cur)
        
        return gcount





            

            


