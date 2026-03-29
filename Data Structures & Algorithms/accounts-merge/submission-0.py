from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        pending = set() # (email, accountName)

        adj = defaultdict(set)

        for a in accounts:
            emails = a[1:]
            pending.update({ (e, a[0]) for e in emails })

            for e in emails:
                adj[e].update(emails)
                
        
        def dfs(node, emails, name):
            
            if (node, name) not in pending:
                return emails
            
            
            pending.remove((node, name))
            emails.add(node)


            for nextNode in adj[node]:
                dfs(nextNode, emails, name)
            
            
            return emails
        
        
        res = []

        while pending:
            
            email, name = pending.pop()
            pending.add((email, name))

            temp = dfs(email, set(), name)
            
            temp2 = [name]
            temp2.extend(sorted(list(temp)))


            res.append(temp2)

        
        return res


