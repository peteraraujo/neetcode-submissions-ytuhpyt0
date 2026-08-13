class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        
        res = []
        cur = []

        def dfs(i=0):
            if i == size:
                res.append(cur[:])
                return

            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()

            while i + 1 < size and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1)
            
        
        dfs()

        return res

