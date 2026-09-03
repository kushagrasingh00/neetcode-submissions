class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

            cur_inc=1   # current increasing strak    
            cur_dec=1   # current decreasing strak
            res=1       # longest streak found

            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    cur_inc+=1
                    cur_dec=1

                elif nums[i] < nums[i-1]:
                    cur_dec+=1
                    cur_inc=1
                else:
                    cur_inc=1
                    cur_dec=1

                # update result on every iteration
                res=max(res,cur_inc,cur_dec)

            return res