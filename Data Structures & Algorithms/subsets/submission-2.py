class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        
        res = []
        cur = []

        def dfs(i=0):

            if i == size:
                res.append(cur[:])
                return

            dfs(i + 1)

            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()

        dfs()
        return res