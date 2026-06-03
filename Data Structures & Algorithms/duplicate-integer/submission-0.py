class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ls_len = len(nums)
        nums_set = set(nums)
        set_len = len(nums_set)

        if ls_len == set_len:
            return False
        return True
        