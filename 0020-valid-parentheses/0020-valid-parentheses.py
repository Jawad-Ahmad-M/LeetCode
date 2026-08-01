class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')' : '(' ,
            '}' : '{' ,
            ']' : '[' 
        }
        for x in s:
            if x in ['(','{','[']:
                stack.append(x)
            if x in [')','}',']']:
                if not stack:
                    return False
                if stack[-1] != mapping[x]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        

        return True