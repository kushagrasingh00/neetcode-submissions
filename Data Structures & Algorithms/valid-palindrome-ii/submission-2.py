class Solution:
    def validPalindrome(self, s: str) -> bool:

            # TRY METHOD -1  -> NON OPTIMAL SOLUTION
        # remove 1 element and re-assess the whole string 
        # do this till the end 

        #  method 2 - 2 pointers Solution
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                removeL, removeR = s[l+1:r+1], s[l:r]
                return removeL == removeL[::-1] or removeR == removeR[::-1]
            
            # Corrected: move l right, move r left
            l += 1
            r -= 1

        return True


