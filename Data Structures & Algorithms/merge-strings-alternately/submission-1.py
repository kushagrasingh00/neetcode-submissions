class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i,j=0,0
        new=[]

        while i < len(word1) and j < len(word2):
            new.append(word1[i])
            new.append(word2[j])
            i+=1
            j+=1

        if i != len(word1):
            new.extend(word1[i:])

        if j != len(word2):
            new.extend(word2[j:])
        
        str="".join(new)
        return str
