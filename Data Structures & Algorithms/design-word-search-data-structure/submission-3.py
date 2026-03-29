class Node:
    def __init__(self):
        self.children = {} # char : Node
        self.end = False

class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        cur = self.head
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            
            cur = cur.children[char]
        
        cur.end = True
        

    def search(self, word: str) -> bool:

        def subsearch(sub, node):
            if not sub and node.end:
                return True
            
            if not sub:
                return False
            char = sub[0]

            if char == ".":
                for option in node.children:
                    if subsearch(sub[1:], node.children[option]):
                        return True
            
            else:
                if char in node.children:
                    return subsearch(sub[1:], node.children[char])
            
            return False
        
        return subsearch(word, self.head)
            
            

            
                

        
