class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        size = len(people)

        l, r = 0, size - 1
        res = 0

        while l <= r:
            ln = people[l]
            rn = people[r]

            both = ln + rn

            if both <= limit:
                l += 1
            
            r -= 1
            res += 1
        
        return res