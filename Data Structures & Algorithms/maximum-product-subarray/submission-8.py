class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minn = maxx  = 1

        for n in nums:
            minn, maxx = min(maxx * n, minn * n, n), max(maxx * n, minn * n, n)
            res = max(res, maxx)

        return res