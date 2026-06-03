from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 统计每个数字出现的频率
        # 例如 nums = [1,1,1,2,2,3], count = {1: 3, 2: 2, 3: 1}
        count = collections.Counter(nums)
        
        # 2. 创建桶数组
        # 最大可能频率是 len(nums)，所以数组长度开辟为 len(nums) + 1
        # freq 的索引代表频率，存放的是对应频率的数字列表
        freq = [[] for _ in range(len(nums) + 1)]
        
        # 3. 将数字根据频率分配到对应的桶中
        for num, c in count.items():
            freq[c].append(num)
            
        # 此时 freq 可能长这样：[ [], [3], [2], [1], [], [], [] ]
        # 索引 1 的位置放着 3 (出现1次)
        # 索引 2 的位置放着 2 (出现2次)
        # 索引 3 的位置放着 1 (出现3次)
        
        # 4. 从高频到低频（从右向左）收集 Top K
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        