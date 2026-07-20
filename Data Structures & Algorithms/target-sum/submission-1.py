class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        size = len(nums)
        res = 0

        visited = {} # (index, current) : combinations

        def dfs(i=-1, current=0):
            query = (i, current)
            
            if query in visited:
                return visited[query]


            if i == size - 1:

                if current == target:
                    return 1

                return 0
            
            l = dfs(i + 1, current + nums[i])
            r = dfs(i + 1, current - nums[i])

            visited[query] = l + r

            return visited[query]
        
        

        return dfs()


