class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        paren_map = {')':'(', ']':'[', '}':'{'}
        
        for item in s:
            if item in ['(', '[', '{']:
                stack.append(item)
            else:
                if not stack:
                    return False
                elif paren_map[item] != stack.pop():
                    return False
        return not stack