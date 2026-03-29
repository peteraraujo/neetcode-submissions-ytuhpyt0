class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        s = []

        i = j = 0

        while i < len(word1) and j < len(word2):
            s.append(word1[i] + word2[j])
            i += 1
            j += 1

        
        return "".join(s) + word1[i:] + word2[j:]

        