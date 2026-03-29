class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def dfs(sub):
            if len(sub) <= 1:
                return sub
            
            m = len(sub) // 2
            h1 = dfs(sub[:m])
            h2 = dfs(sub[m:])

            res = []
            while h1 or h2:
                if not h1:
                    res.extend(h2[::-1])
                    break
                elif not h2:
                    res.extend(h1[::-1])
                    break
                elif h1[-1] <= h2[-1]:
                    res.append(h1.pop())
                else:
                    res.append(h2.pop())
            
            return res[::-1]
        
        return dfs(nums)[::-1]