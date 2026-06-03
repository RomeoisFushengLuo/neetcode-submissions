class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Hashmap is used to optimize the time complexity to O(n)
        """
        hashmap = {} # store {value: index}
        for i in range(len(nums)):
            to_find = target - nums[i]
            if to_find in hashmap.keys():
                return [i, hashmap[to_find]] if i < hashmap[to_find] else [hashmap[to_find], i] # (index, other index)
            else:
                hashmap[nums[i]] = i