class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        

        new=[]
        l , r = 0 , len(nums)-1

        while l <= r:
            
            if nums[l]*nums[l] > nums[r]*nums[r]:
                new.append(nums[l]*nums[l])
                l+=1
            else:
                new.append(nums[r]*nums[r])
                r-=1

        return new[::-1]

