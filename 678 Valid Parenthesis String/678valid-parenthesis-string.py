class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1 = [] # index of "("
        stack2 = [] # index of "*"

        for i, char in enumerate(s):
            if char == "(":
                stack1.append(i)
            elif char == ")":
                if not stack1 and not stack2:
                    return False
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
            else:
                stack2.append(i)

        # check if star appears before "(":
        while stack1 and stack2:
            if stack1.pop() > stack2.pop():
                return False
            
        return not stack1

# Time: O(n)
# Space: O(n)