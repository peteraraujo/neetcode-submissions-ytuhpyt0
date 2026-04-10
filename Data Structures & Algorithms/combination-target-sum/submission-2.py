class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        visited = set() # ()

        def dfs(state = [0] * len(nums), cur = [], s = 0):

            if s > target or tuple(state) in visited:
                return
            
            if s == target:
                res.append(cur.copy())
                visited.add(tuple(state))
                return
            
            for i in range(len(nums)):
                n = nums[i]

                cur.append(n)
                s += n
                state[i] += 1

                dfs(state, cur, s)

                cur.pop()
                s -= n
                state[i] -= 1
        
        dfs()
        return res
            
