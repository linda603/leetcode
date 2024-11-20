class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for string in tokens:
            if string not in "+-*/":
                stack.append(int(string))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if string == "+":
                    stack.append(num1 + num2)
                elif string == "-":
                    stack.append(num1 - num2)
                elif string == "*":
                    stack.append(num1 * num2)
                elif string == "/":
                    stack.append(int(num1 / num2))
        return stack[0]

# Time: O(n)
# Space: O(n)
