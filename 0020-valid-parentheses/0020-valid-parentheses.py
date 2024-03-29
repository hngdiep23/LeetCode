class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '(' or char == "[" or char == "{":
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ')' and stack[-1] == "(":
                    stack.pop()
                elif char == ']' and stack[-1] == "[":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return not stack 
solution = Solution()
s = "[()[]]{}"
print(solution.isValid(s))