class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        
        special = ["+","C","D"]
        res =[]
        final=0
        for i in operations:
            if i in special:
                if i == "+":
                    res.append(int(res[-1])+int(res[-2]))
                elif i == "C":
                    res.pop()
                else:
                    res.append(int(res[-1]*2))

            else:
                res.append(int(i))

        for x in res:
            final+=int(x)
        
        return final