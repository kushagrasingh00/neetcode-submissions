class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # trivial Solution

        new=[]
        # making a new squared list
        for i in range(len(nums)):
            new.append(nums[i]*nums[i])
        
        # by 2-pointers -> sorting the new list
        for l in range(len(new)):
            for r in range(l+1,len(new)):
                if new[r] < new[l]:
                    new[l], new[r] = new[r] , new[l]
        
        return new

