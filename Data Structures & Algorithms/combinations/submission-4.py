class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def dfs(cur = []):
            if len(cur) == k:
                res.append(cur.copy())
                return
            
            for num in range(cur[-1] + 1 if cur else 1, n + 1):
                cur.append(num)
                dfs(cur)
                cur.pop()
            
        dfs()
        return res




            

            
