class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        max_dec = 1
        max_inc = 1
        curr_inc = 1
        curr_dec = 1
        for i in range(1 , len(nums)):
            if nums[i] > nums[i-1]: 
                curr_inc += 1
                curr_dec = 1
                if curr_inc > max_inc:
                    max_inc = curr_inc


            elif nums[i] < nums[i-1]:
                curr_dec += 1
                curr_inc = 1
                if curr_dec > max_dec:
                    max_dec=curr_dec
            else:
                curr_dec = 1
                curr_inc = 1
        
        if max_dec > max_inc:
            return max_dec
        else:
            return max_inc




