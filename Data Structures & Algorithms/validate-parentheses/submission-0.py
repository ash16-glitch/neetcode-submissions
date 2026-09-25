class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '{':
                stack.append('}')
            elif i == '[':
                stack.append(']')
            else:
                if not stack:
                    return False
                
                popitem = stack.pop()
                if popitem != i:
                    return False
        return not stack
        