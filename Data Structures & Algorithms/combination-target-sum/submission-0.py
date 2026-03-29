class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = set()
        temp = []

        def dfs(i):

            if i >= len(nums):
                return

            # Base: sum of temp is == target
            if sum(temp) == target:
                res.add(tuple(temp))
                return

            # Case 1: If sum of temp is greater than target

            # Case 2: Add the same number
            if sum(temp) + nums[i] <= target:
                temp.append(nums[i])
                dfs(i)
                temp.pop()

            # Case 3: Add next number
            if i + 1 < len(nums) and sum(temp) + nums[i + 1] <= target:
                temp.append(nums[i + 1])
                dfs(i + 1)
                temp.pop()
            
            dfs(i + 1)
        
        dfs(0)
        return list(map(list, res))
