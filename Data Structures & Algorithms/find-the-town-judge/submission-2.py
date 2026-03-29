class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        level = [0] * n

        for a, b in trust:
            level[a - 1] -= 1
            level[b - 1] += 1
        
        for i in range(n):
            if level[i] == n - 1:
                return i + 1
        return -1