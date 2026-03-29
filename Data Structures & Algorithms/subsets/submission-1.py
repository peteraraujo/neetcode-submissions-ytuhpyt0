class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        temp = []

        def dfs(i):

            # Base case
            if i >= len(nums):
                res.append(temp.copy())
                return
            
            # Case 1: We add the item
            temp.append(nums[i])
            dfs(i + 1)
            temp.pop()

            # Case 2: We don't add the item
            dfs(i + 1)
        
        dfs(0)
        return res
