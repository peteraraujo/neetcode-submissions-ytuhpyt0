class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        size = len(nums)
        
        total = sum(nums)

        if total % 2 != 0:
            return False;

        target = total // 2

        cache = set() # (start, current)

        def dfs(start = 0, current = 0):
            st = (start, current)

            if current > target or st in cache:
                return False
            
            if current == target:
                return True
            
            cache.add(st)

            for i in range(start, size):
                
                if dfs(i + 1, current + nums[i]):
                    return True
            
            return False

        
        return dfs()


        
