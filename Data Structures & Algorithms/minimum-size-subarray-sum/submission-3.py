class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        res = 0

        pre = [0] * (size + 1)

        for i in range(size):
            pre[i + 1] = pre[i] + nums[i]

        print(pre)


        for i in range(size):
            wz = 0

            for j in range(i, size):

                if pre[j+1] - pre[i] >= target:
                    break
            else:
                continue
            
            if not res:
                res = (j+1)-i
            else: 
                res = min(res, (j+1)-i)
        
        return res


        




