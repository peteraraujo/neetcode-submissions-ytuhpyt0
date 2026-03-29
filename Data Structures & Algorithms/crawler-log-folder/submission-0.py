class Solution:
    def minOperations(self, logs: List[str]) -> int:
        loc = []

        for l in logs:
            if l == "../":

                if loc:
                    loc.pop()

            elif l != "./":
                loc.append(l)
        
        return len(loc)





