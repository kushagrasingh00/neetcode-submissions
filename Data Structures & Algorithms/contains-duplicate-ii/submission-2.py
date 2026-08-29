class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window=set()

        L=0

        for R in range(len(nums)):
        
            # checking bounds for sliding window
            if R - L > k:
                window.remove(nums[L])
                L+=1

            # if num in set -> duplicate found -> within bounds
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False

                

