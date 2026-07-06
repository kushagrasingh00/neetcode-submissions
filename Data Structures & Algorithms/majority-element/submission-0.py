class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts={}
        length = len(nums)/2
        
        #making dict
        for num in nums:
            counts[num]= counts.get(num,0) +1
        
        #accessing dict for key value pair
        for key , value in counts.items():
            if value > length:
                return key