class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target=len(nums)/2
        freq={}
        
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1

        for key,value in freq.items():
            if value >= target:
                return key