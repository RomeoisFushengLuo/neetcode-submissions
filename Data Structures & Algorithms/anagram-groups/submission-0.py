from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26 # 26 char in total: a-z
            for c in s:
                count[ord(c) - ord('a')] += 1 

            ans[tuple(count)].append(s)
        
        return list(ans.values())
        