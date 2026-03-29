class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k %= size

        l, r = 0, size - 1

        def rotate(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        rotate(0, size - 1)
        rotate(0, k - 1)
        rotate(k, size - 1)

        