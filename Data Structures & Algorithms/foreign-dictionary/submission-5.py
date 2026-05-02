from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        if len(words) < 2:
            return "".join(words)

        adj = defaultdict(list)

        for i in range(len(words) - 1):
            wa, wb = words[i], words[i + 1]

            added = False

            for wi in range(max(len(wa), len(wb))):

                if wi < len(wa):
                    adj[wa[wi]]
                
                if wi < len(wb):
                    adj[wb[wi]]

                if not added and wi >= len(wb):
                    return ""
                

                if not added and wi < len(wa) and wi < len(wb) and wa[wi] != wb[wi]:
                    adj[wb[wi]].append(wa[wi])
                    added = True
                
            
        res = []
        added = set()

        # Returns True if no cycle detected; False otherwise.
        def dfs(node, visited):
            if node in visited:
                return False
            if node in added:
                return True
            
            visited.add(node)

            if node in adj:
                for nei in adj[node]:
                    if not dfs(nei, visited):
                        return False
            
            res.append(node)
            added.add(node)
            visited.remove(node)

            return True
        
        for node in adj:
            if not dfs(node, set()):
                return ""
        
        return "".join(res)
            
        



