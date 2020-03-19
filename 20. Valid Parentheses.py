class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack:
                    op = stack.pop()
                    if op == '[' and c == ']':
                        continue
                    elif op == '{' and c == '}':
                        continue
                    elif op == '(' and c == ')':
                        continue                        
                    else:
                        return False
                else:
                    return False
        
        if stack:
            return False
       
        return True