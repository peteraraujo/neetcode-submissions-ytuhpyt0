class Solution:
    def insert(self, ins: List[List[int]], nin: List[int]) -> List[List[int]]:

        res = []
        
        for i in range(len(ins)):
            interval = ins[i]

            if interval[1] < nin[0]:
                res.append(interval)
                continue

            break

        else:
            res.append(nin)
            return res

        for i in range(i, len(ins)):
            interval = ins[i]

            if interval[0] <= nin[1]:
                nin[0] = min(nin[0], interval[0])
                nin[1] = max(nin[1], interval[1])
                continue
            
            break
        else:
            res.append(nin)
            return res
        
        res.append(nin)
        res.extend(ins[i:])
        return res