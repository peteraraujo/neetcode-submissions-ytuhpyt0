class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)

        res = set()
        cur = []
        
        def dfs(i=0):
            if i == size:
                res.add(tuple(sorted(cur)))
                return
            
            dfs(i + 1)

            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
        
        dfs()

        return list(res)