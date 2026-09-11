class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1

            else:
                # remove l
                removeL= s[l+1 : r+1]
                # remove r
                removeR= s[l:r]

                return removeL == removeL[::-1] or removeR == removeR[::-1]
        
        return True
        