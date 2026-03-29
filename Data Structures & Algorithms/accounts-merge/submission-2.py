from collections import defaultdict

class DS:
    def __init__(self, emails):
        self.parent = {}
        self.rank = {}

        for email in emails:
            self.parent[email] = email
            self.rank[email] = 0
    
    def __repr__(self):
        return str(self.parent)
    
    
    def findParent(self, node):
        cur = node

        while cur != self.parent[cur]:
            cur = self.parent[cur]

            # Path compression
            self.parent[cur] = self.parent[self.parent[cur]]
        
        return cur
    
    def union(self, a, b):
        pa, pb = self.findParent(a), self.findParent(b)

        if pa == pb:
            return False
        
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        else:
            self.parent[pa] = pb
            self.rank[pb] += 1
        
        return True





class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = set()
        emailToAccount = {}

        for acc in accounts:
            accname = acc[0]
            for i in range(1, len(acc)):
                emails.add(acc[i])
                emailToAccount[acc[i]] = accname
        
        ds = DS(emails)

        for acc in accounts:
            for i in range(1, len(acc) - 1):
                a, b = acc[i], acc[i + 1]

                ds.union(a, b)
        
        inv = defaultdict(list)


        for e in emails:
            inv[ds.findParent(e)].append(e)

        res = []

        for parentemail, emaillist in inv.items():
            accname = emailToAccount[parentemail]
            temp = [accname]
            temp.extend(emaillist)
            res.append(temp)
        
        return res






        