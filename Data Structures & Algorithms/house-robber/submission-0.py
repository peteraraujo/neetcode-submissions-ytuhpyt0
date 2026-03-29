class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # Go over all the numbers
        for num in nums:
            
            # Select the max posibility.
            # Posibility 1: You choose the max amount up to 2 positions before and we add the amount of this position.
            # The reason why we go 2 positions before is because we cant have adjacent numbers
            # Posibility 2: You choose the position before the current 1. However, this means we cant add the current position.
            temp = max(num + rob1, rob2)

            # Here we prepare the variables for the next iteration
            # First we move rob2 to rob1.
            # This is because rob1 is the one that is not next to the current value
            # Since we are moving one item to the right, we also move rob
            rob1 = rob2

            # Now rob2 passes to be out temp value
            # Same reason as before, we are moving to the right. So our current num will be the number that is the next to the "next current"
            rob2 = temp
        
        # This should the max
        return rob2