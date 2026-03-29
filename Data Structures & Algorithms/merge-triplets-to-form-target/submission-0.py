class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        t1 = t2 = t3 = False

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            if not t1 and t[0] == target[0]:
                t1 = True
            
            if not t2 and t[1] == target[1]:
                t2 = True

            if not t3 and t[2] == target[2]:
                t3 = True


        return t1 and t2 and t3


