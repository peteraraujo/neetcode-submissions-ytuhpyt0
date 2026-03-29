class Solution:
    def canJump(self, nums: List[int]) -> bool:

        closest = len(nums) - 1

        for i in range(len(nums) - 2 , 0, -1):
            if i + nums[i] >= closest:
                closest = i

        return nums[0] >= closest





