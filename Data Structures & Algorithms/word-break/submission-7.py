class Trie:
    def __init__(self, char):
        self.children = {} # char : node
        self.char = char
        self.end = False
    
    def __repr__(self):
        return f"{self.char} -> {[self.children.values()]}"


def populate(root, words):
    
    for word in words:

        current = root

        for char in word:

            if char not in current.children:
                current.children[char] = Trie(char)

            current = current.children[char]
        
        current.end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)

        root = Trie(0)
        populate(root, wordDict)
        
        visited = set([0])
        starts = [0]

        while starts:
            index = starts.pop()
            current = root

            while index < size and (char := s[index]) in current.children:
                current = current.children[char]

                if current.end:
                    if index + 1 == size:
                        return True
                    
                    if index + 1 not in visited:
                        starts.append(index + 1)
                        visited.add(index + 1)

                index += 1
        
        return False

