class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack=[]

        for i in logs:
            if len(stack) > 0 and i == "../":
                stack.pop()
            elif len(stack) == 0 and i == "../":
                continue
            elif i == "./":
                continue
            else:
                stack.append(i)

        return (len(stack))