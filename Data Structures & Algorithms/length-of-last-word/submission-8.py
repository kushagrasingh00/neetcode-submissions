class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0
        
        i = len(s)-1

        while i >= 0:
            if s[i] == " " and length == 0:
                i-=1
            
            elif s[i].isalnum():
                length+=1
                i-=1

            elif s[i] ==  " " and length !=0:
                break

        return length