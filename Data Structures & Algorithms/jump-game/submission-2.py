class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        memo = [False] * len(nums)
        memo[-1] = True

        closest = len(nums) - 1

        for i in range(len(nums) - 2 ,-1, -1):
            print("Index:", i)
            print("nums[i]:", nums[i])
            print("closest:", closest)
            print("Sum:",  i + nums[i])
            if i + nums[i] >= closest:
                print("True")
                memo[i] = True
                closest = i
        
        print(memo)
        return memo[0]
            





