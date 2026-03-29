class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = -1
        for i in range(min(list(map(lambda x: len(x), strs)))):
            cur = strs[0][i]
            for j in range(1, len(strs)):
                if cur != strs[j][i]:
                    return strs[0][:i]
        
        return "" if i == -1 else strs[0][:i+1]
