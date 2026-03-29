class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, o, c):
            if o == 0 and c == 0:
                res.append(cur)
                return
            
            if o > 0:
                dfs(cur + "(", o - 1, c + 1)
            if c > 0:
                dfs(cur + ")", o, c - 1)
        
        dfs("", n, 0)
        return res
            
            
