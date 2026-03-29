class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # Check if there is enough gas in total to complete the circut
        if sum(gas) < sum(cost):
            return -1
        
        # Keep track of total gas
        total = 0

        # Keep track of initial position
        res = 0

        # Iterate over the array
        for i in range(len(gas)):

            # Calculate the total of gas in current index
            total += (gas[i] - cost[i])

            # If it is negative, restart total and move initial position to next index
            if total < 0:
                total = 0
                res = i + 1
        
        # Return initial position
        return res