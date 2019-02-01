class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        stack=[]
        for i in s:
            if i=='[' or i=='(' or i=='{':
                stack.append(i)
                continue
            if i==')' :
                if'(' not in stack:
                    return False
                if'('==stack[-1]:
                    stack.pop()
                else:
                    return False   
            if i=='}' :
                if'{' not in stack:
                    return False
                if'{'==stack[-1]:
                    stack.pop()
                else:
                    return False
            if i==']' :
                if'[' not in stack:
                    return False
                if'['==stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:   #key
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
