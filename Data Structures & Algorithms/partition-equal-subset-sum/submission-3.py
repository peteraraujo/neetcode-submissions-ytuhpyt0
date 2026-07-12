class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2

        nums.sort()



        def dfs(s, start):

            if s == target:
                return True

            if s > target:
                return False
            
            for i in range(start, size):
                n = nums[i]
                
                if dfs(s + n, i + 1):
                    return True
            
            return False
        

        return dfs(0, 0)


