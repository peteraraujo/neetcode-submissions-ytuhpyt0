from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        ady = defaultdict(set)

        for a, b in prerequisites:
            ady[a].add(b)

        pres = defaultdict(set)

        def dfs(node):
            if node in pres:
                return pres[node]

            for b in ady[node]:
                pres[node].add(b)
                pres[node].update(dfs(b))
            
            return pres[node]
        
        for i in range(numCourses):
            dfs(i)
        

        return list(map(lambda x: x[1] in pres[x[0]] , queries))
            
            
            
            
