class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)

        maxx = minn = 1

        for n in nums:
            if n == 0:
                maxx = minn = 1
                continue
            
            maxx, minn = max(maxx * n, minn * n, n), min(maxx * n, minn * n, n)
            res = max(res, maxx)
        
        return res


            


        




