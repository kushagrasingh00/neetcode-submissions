class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            right_sum = 0
            left_sum = 0
            for j in range(i+1 , len(nums)):
                right_sum += nums[j]
            
            for k in range(i-1 , -1 , -1):
                left_sum += nums[k]
            
            if right_sum == left_sum:
                return i
        
        else :
            return -1