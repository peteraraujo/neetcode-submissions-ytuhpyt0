class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Keep track to closest possible solution path
        closest = len(nums) - 1

        # Iterate from second to last to second item.
        # Skip last because that is the index goal and it is already set as closest
        # It will always be true.
        # Skip first because we are evaluating that one on the return expression.
        for i in range(len(nums) - 2 , 0, -1):

            # Here we check if the index can jump at least to the closest valid index.
            if i + nums[i] >= closest:

                # If so, we update the closest value, because we have a new one.
                closest = i

        # The excercise asks whether the first index and reach the last one.
        # So we check this here. Same logic as with other indices.
        return nums[0] >= closest