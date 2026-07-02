class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)

        wordDict = set(wordDict)

        visited = set([0])
        starts = [0]

        while starts:
            startIndex = starts.pop()

            for i in range(startIndex, size):
                word = s[startIndex:i+1]

                if word in wordDict:
                    if i + 1 == size:
                        return True

                    if i + 1 not in visited:
                        starts.append(i + 1)
                        visited.add(i + 1)
        
        return False
                    