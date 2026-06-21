class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size = len(s)

        res = ""

        tc = Counter(t)
        tchars = tc.keys()
        sc = Counter()

        l = 0

        def checkMatch():
            for tchar in tchars:
                if tchar not in sc or sc[tchar] < tc[tchar]:
                    return False
            
            return True

        for r in range(size):
            char = s[r]

            sc[char] += 1


            while l <= r and (s[l] not in tchars or sc[s[l]] > tc[s[l]]):
                sc[s[l]] -= 1
                l += 1

            if checkMatch():
                if not res or (r - l) + 1 < len(res):
                    res = s[l:r+1]
        
        return res