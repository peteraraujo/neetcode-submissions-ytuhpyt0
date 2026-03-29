class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k %= size

        for i in range(size//2):
            nums[i], nums[(size - 1) - i] = nums[(size - 1) - i], nums[i]


        for i in range(k//2):
            nums[i], nums[(k - 1) - i] = nums[(k - 1) - i], nums[i]
        

        for i in range((size-k)//2):

            i += k

            print(f"{i=} | {((size - 1) - (i-k))=}")


            nums[i], nums[(size - 1) - (i-k)] = nums[(size - 1) - (i-k)], nums[i]