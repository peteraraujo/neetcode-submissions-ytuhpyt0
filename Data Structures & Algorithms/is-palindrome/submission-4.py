import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"\W", "", s).lower()
        rev = "".join(reversed(s))
        return rev == s