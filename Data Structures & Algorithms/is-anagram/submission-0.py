from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_coun = Counter(s)
        t_coun = Counter(t)

        if s_coun == t_coun:
            return True
        return False
        