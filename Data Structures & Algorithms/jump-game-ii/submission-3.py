class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        n = len(nums)
        memo = [[False, 0] for _ in range(n)]
        memo[-1] = [True, 0]

        closest = n - 1

        for i in range(n - 2, 0, -1):
            if i + nums[i] < closest:
                continue
            
            closest = i
            memo[i][0] = True

            minSteps = min(
                filter(
                    lambda x: x[0] == True,
                    memo[i+1:min(n - 1, i + nums[i])+1]
                    ),
                key=lambda x: x[1]
                )[1]
            memo[i][1] = minSteps + 1

            print("Index:", i)
            print(memo)
        
        return min(
            filter(
                lambda x: x[0] == True,
                memo[1:nums[0]+1]
                ),
            key=lambda x: x[1]
            )[1] + 1


