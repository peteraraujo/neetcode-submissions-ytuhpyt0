class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        if not nums:
            return [[lower, upper]]
        
        res = []

        if lower < nums[0]:
            res.append([lower, nums[0] - 1])
        
        for i in range(1, len(nums)):
            prev = nums[i - 1]
            num = nums[i]

            if num - 1 > prev:
                res.append([prev + 1, num - 1])


        if upper > nums[-1]:
            res.append([nums[-1] + 1, upper])

        return res