class TreeNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()


    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.isEnd = True


    def search(self, word: str) -> bool:


        def look(node, word) -> bool:

            cur = node

            for i, c in enumerate(word):

                if c != '.':
                    if c not in cur.children:
                        return False
                    else:
                        cur = cur.children[c]
                        continue
                else:
                    for child in cur.children.values():
                        result = look(child, word[i+1:])
                        if result:
                            return True
                    return False

            return cur.isEnd

        return look(self.root, word)