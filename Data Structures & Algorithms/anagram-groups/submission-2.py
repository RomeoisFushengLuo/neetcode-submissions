from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 使用 defaultdict(list) 可以省去判断 key 是否存在的麻烦
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26  # 初始化一个全 0 的长度为 26 的列表
            for c in s:
                # ord(c) - ord('a') 可以把 'a' 映射到 0，'b' 映射到 1，以此类推
                count[ord(c) - ord('a')] += 1
            
            # 将 list 转换为 tuple，此时它变得可哈希，可以作为 Key 啦！
            # 例如 "aba" 会生成 (2, 1, 0, 0, ..., 0)
            ans[tuple(count)].append(s)
            
        return list(ans.values())
        