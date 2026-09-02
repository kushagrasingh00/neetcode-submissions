class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
       
        max_sum=0
        sum=0
        for i in range(len(nums)):
            if i == 0:
                sum+=nums[i]
                if sum > max_sum:
                    max_sum = sum
            elif nums[i] > nums[i-1]:
                sum+=nums[i]
                if sum > max_sum:
                    max_sum = sum
            else:
                sum = nums[i]
        
        return max_sum