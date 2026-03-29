class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, ops):
            if not ops:
                res.append(cur.copy())
            

            for o in ops:
                ops.remove(o)
                cur.append(o)

                dfs(cur, ops.copy())


                ops.add(o)
                cur.pop()
        
        dfs([], set(nums))
        return res

