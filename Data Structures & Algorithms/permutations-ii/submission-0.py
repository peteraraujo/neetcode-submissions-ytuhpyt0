class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        visited = set()
        

        def dfs(options={ (nums[i], i) for i in range(len(nums)) }, stack=[]):
            
            snapshot = tuple(stack)

            if snapshot in visited:
                return
            
            visited.add(snapshot)

            if not options:
                res.append(stack.copy())
                return
            
            for opt in options.copy():
                options.remove(opt)
                stack.append(opt[0])
                
                dfs(options, stack)
                
                stack.pop()
                options.add(opt)
        

        dfs()
        return res

        
        
