class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Var to keep track of max value. Starts at first item, as it is warranted there is at least one item in nums.
        maxSum = nums[0]

        # Current sum is 0 as starting value
        curSum = 0

        # Iterate over nums
        for n in nums:

            # Check if curSum is negative
            if curSum < 0:

                # If so, reset it to 0
                curSum = 0

            # Add current number to curSum
            curSum += n

            # Update maxSum
            maxSum = max(maxSum, curSum)

        # Return final value
        return maxSum

