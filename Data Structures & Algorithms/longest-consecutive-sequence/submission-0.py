class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        longest = 0

        for num in nums:

            # If the last digit of the current value does not exist, then the current value is a valid starting point
            if (num-1) not in nums_set:
                current_num = num
                cur_longest = 1

                while (current_num+1) in nums_set:
                    cur_longest += 1
                    current_num += 1 
                longest = max(longest, cur_longest)
        
        return longest

        