class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        i=0
        max_count=0
        count=0
        while i < len(nums):
            
            if nums[i] != 0:
                count +=1
                i+=1

                if count>max_count:
                    max_count = count

            else:
                count=0
                i+=1
        
        return max_count