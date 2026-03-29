class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Node()

        for word in dictionary:
            cur = trie

            for char in word:
                if char not in cur.children:
                    cur.children[char] = Node()
                
                cur = cur.children[char]
            
            cur.end = True
        
        size = len(s)
        extras = [0] * (size + 1)

        for i in range(size - 1, -1, -1):
            maxadvance = 0
            minextras = 1 + extras[i + 1]
            cur = trie

            for j in range(i, size):
                if s[j] in cur.children:
                    cur = cur.children[s[j]]

                    if cur.end and extras[j + 1] < minextras:
                        minextras = extras[j + 1]
                        maxadvance = (j - i) + 1
                else:
                    break
            
            if maxadvance == 0:
                extras[i] = extras[i + 1] + 1
            else:
                extras[i] = extras[i + maxadvance]

        print(extras)        
        return extras[0]

