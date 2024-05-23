class Solution:
    def isValid(self, s: str) -> bool:
        matching_pair = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            if c in matching_pair:
                top_element = stack.pop() if stack else '#'
                if matching_pair[c] != top_element:
                    return False
            else:
                stack.append(c)
        return not stack
        
