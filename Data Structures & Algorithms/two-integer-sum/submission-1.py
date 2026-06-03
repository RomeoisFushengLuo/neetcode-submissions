class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        needed_nums = [target - ele for ele in nums]

        for i in range(len(needed_nums)):
            try:
                idx = nums.index(needed_nums[i], i+1)
                return [i, idx]
            except ValueError:
                continue
                

        