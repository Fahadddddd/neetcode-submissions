class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append('(')
            elif ch == '{':
                stack.append('{')
            elif ch == '[':
                stack.append('[')
            
            else:
                if not stack:
                    return False
                
                top = stack.pop()

                if ch == ')' and top != '(':
                    return False
                elif ch == '}' and top != '{':
                    return False
                elif ch == ']' and top != '[':
                    return False
        return len(stack) == 0
