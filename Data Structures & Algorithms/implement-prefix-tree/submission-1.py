class Node:
    def __init__(self, val):
        self.val = val
        self.children = {} # char : Node
        self.end = False



class PrefixTree:

    def __init__(self):
        self.head = Node(None)
        

    def insert(self, word: str) -> None:
        cur = self.head
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node(c)
            
            cur = cur.children[c]
        
        cur.end = True


    def search(self, word: str) -> bool:
        cur = self.head
        for c in word:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        
        return cur.end
        


    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for c in prefix:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        
        return True

        
        