class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def dfs(stack=[]):
            if len(stack) == k:
                res.append(stack.copy())
                return
            
            last = stack[-1] if stack else 0

            for e in range(last + 1, n + 1):
                stack.append(e)
                dfs(stack)
                stack.pop()
            
        dfs()
        
        return res
