class Node:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def __repr__(self):
        return f"{self.children} | {self.word}"

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        trie = Node()
        failed = set() # failed idxs

        for w in wordDict:
            cur = trie
            for c in w:
                if c not in cur.children:
                    cur.children[c] = Node()
                cur = cur.children[c]
            cur.word = True
        

        def dfs(i=0):
            if i == size:
                return True
            if i in failed:
                return False
            cur = trie
            
            for idx in range(i, size):
                char = s[idx]

                if char not in cur.children:
                    failed.add(i)
                    return False
                
                cur = cur.children[char]

                if cur.word and dfs(idx + 1):
                    return True

            failed.add(i)
            return False
        
        return dfs()
                    

        