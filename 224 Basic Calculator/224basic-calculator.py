class Solution:
    def calculate(self, s: str) -> int:
        
        def dfs(i):
            def update(val, op):
                if op == "+":
                    stack.append(val)
                elif op == "-":
                    stack.append(-val)

            val = 0
            op = "+"
            stack = []

            while i < len(s):
                if s[i].isdigit():
                    val = val * 10 + int(s[i])
                elif s[i] in "+-":
                    update(val, op)
                    op = s[i]
                    val = 0
                elif s[i] == "(":
                    val, j = dfs(i + 1)
                    i = j
                elif s[i] == ")":
                    update(val, op)
                    return [sum(stack), i]
                i += 1
            update(val, op)
            return [sum(stack), i + 1]
    
        return dfs(0)[0]

# Time: O(n). Each char is processed once
# Space: O(n)