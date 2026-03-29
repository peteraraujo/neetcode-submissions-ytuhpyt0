class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isAnagram(s1, s2):
            if len(s1) != len(s2):
                return False
            
            d = [0] * 26
            b = ord("a")
            for c in s1:
                d[ord(c) - b] += 1

            for c in s2:
                d[ord(c) - b] -= 1
                if d[ord(c) - b] < 0:
                    return False
            return True
        
        groups = {} # { 1: [["", ""], ["", ""]], }

        for s in strs:
            l = len(s)

            if (groupList := groups.get(l)):

                for anagramList in groupList:
                    if (isAnagram(s, anagramList[0])):
                        anagramList.append(s)
                        break
                else:
                    groupList.append([s])
            else:
                groups[l] = [[s]]
        
    
        return [ anagramGroup for groupList in groups.values() for anagramGroup in groupList ]



