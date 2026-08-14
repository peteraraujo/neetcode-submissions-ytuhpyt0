class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        cs = Counter(people)


        l, r = min(people), max(people)
        res = 0

        while l <= r:
            while l <= r and cs[r] == 0:
                r -= 1
            
            if not l <= r or cs[r] == 0:
                break

            while l <= r and cs[l] == 0:
                l += 1
            
            both = l + r

            if both <= limit:
                cs[l] -= 1
            
            if cs[r] > 0:
                cs[r] -= 1
            res += 1
            


        return res