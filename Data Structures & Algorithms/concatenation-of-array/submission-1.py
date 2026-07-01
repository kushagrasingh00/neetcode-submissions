class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k=True
        ans=[]
        while k == True:
            for i in nums:
                ans.append(i)
            if len(ans)==2*(len(nums)):
                k=False
        return ans