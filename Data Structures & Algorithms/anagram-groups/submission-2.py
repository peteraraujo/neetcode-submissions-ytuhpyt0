class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        groups = defaultdict(list)
        base = ord('a')

        for a in strs:

            counters = [0] * 26

            for c in a:
                counters[ord(c) - base] += 1


            groups[tuple(counters)].append(a)
        
        return list(groups.values())







