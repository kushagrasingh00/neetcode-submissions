class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        # first time solution 

        sorted_nums = sorted(nums)

        left = 0
        min_val = float("inf")  

        curr = []

        for right in range(len(sorted_nums)):
            curr.append(sorted_nums[right])

            # window exceeds k
            if right - left + 1 > k:
                curr.pop(0)
                left += 1

            # window completed -> evaluate
            if right - left + 1 == k:
                value = curr[-1] - curr[0]
                min_val = min(value, min_val)

        return min_val