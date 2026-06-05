class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Anagrams
        ags = defaultdict(list) # tuple of count : list of words

        for word in strs:
            footprint = [0] * 26

            for letter in word:
                footprint[ord(letter) - ord("a")] += 1
            
            ags[tuple(footprint)].append(word)
        
        return list(ags.values())
            