class Solution:
    def isValid(self, s: str) -> bool:


        stack =[]
        map = {")": "(", "]": "[", "}": "{"}

        for c in s:
            # if c -> closing bracket -> go inside map 
            # if c -> opening bracket -> add to stack

            if c in map:
                if len(stack) > 0 and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)
        
        # after the loop ends if the stack is empty ie all opening brackets were closed accordingly 
        if len(stack) == 0:
            return True
        else:
            return False
                
