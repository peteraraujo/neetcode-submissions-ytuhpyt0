class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        size = len(nums)
        nums.sort()

        items = []
        cursum = 0

        res = []

        def dfs(i):
            nonlocal cursum
            
            if cursum > target:
                return False
            if cursum == target:
                res.append(items.copy())
                return False

            
            for ni in range(i, size):
                
                val = nums[ni]
                cursum += val
                items.append(val)

                cont = True
                if not dfs(ni):
                    cont = False

                cursum -= val
                items.pop()

                if not cont:
                    break

            
            return True
        
        dfs(0)
        return res
