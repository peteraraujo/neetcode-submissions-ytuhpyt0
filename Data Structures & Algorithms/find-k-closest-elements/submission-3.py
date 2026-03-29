class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        size = len(arr)
        if k >= size:
            return arr
        
        l, r = 0, size - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] < x:
                l = m + 1
            else:
                r = m - 1

        r = l
        l -= 1

        if l == -1:
            return arr[:k]

        for _ in range(k):
            print(f"{l=} | {r=}")
            if r >= size:
                return arr[(size - 1) - (k-1):]
            if l == -1:
                return arr[:k]
            
            a = arr[l]
            b = arr[r]

            if abs(a) == abs(b) or abs(a - x) <= abs(b - x):
                l -= 1

            else:
                r += 1
        
        print(f"{l=} | {r=}")
        return arr[l+1:r]




        



        

        