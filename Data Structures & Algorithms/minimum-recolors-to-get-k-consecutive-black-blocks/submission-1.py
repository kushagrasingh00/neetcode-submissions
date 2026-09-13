class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        l=0
        min_count=float("inf")
        count=0

        for r in range(len(blocks)):

            if blocks[r] == 'W':
                count += 1

            if r - l + 1 > k:
                if blocks[l] == 'W':
                    count -= 1
                l += 1 

            if r - l + 1 == k:
                min_count = min(min_count , count)

        return min_count