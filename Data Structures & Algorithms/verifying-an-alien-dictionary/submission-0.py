class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        size = len(words)
        if size == 1:
            return True

        letters = { order[i]:i for i in range(len(order)) }
        print(letters)

        for i in range(size - 1):
            a = words[i]
            b = words[i + 1]

            j = 0
            while j < len(a) or j < len(b):
                if j >= len(b):
                    return False
                elif j >= len(a):
                    break

                orda = letters[a[j]]
                ordb = letters[b[j]]

                if orda < ordb:
                    break
                if orda > ordb:
                    return False
                
                j += 1
        
        return True
            








