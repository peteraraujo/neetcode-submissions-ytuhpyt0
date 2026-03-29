class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        valid = [True] * n
        trusted = [0] * n

        for a, b in trust:
            valid[a - 1] = False
            trusted[b - 1] += 1

        print(f"{trusted=} | {valid=}")
        for i in range(n):
            t = trusted[i]
            if t == n - 1 and valid[i]:
                return i + 1
        
        return -1

            

         





