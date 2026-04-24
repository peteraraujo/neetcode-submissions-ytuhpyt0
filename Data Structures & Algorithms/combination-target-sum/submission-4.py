class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)
        nums.sort()        
        
        res = []

        # Returns Continue boolean flag (True/False)
        def dfs(cur=0, stack=[]):
            if cur == target:
                res.append([nums[i] for i in stack])
                return False
            if cur > target:
                return False
            
            for i in range(stack[-1] if stack else 0, size):
                stack.append(i)
                cur += nums[i]

                cont = dfs(cur, stack)
                
                stack.pop()
                cur -= nums[i]

                if not cont:
                    break
            
            return True
        
        dfs()

        return res
            
                

            