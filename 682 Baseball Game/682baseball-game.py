class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:
            if len(stack) >= 2 and op == '+':
                stack.append(stack[-1] + stack[-2])
            elif len(stack) >= 1 and op == 'D':
                stack.append(stack[-1] * 2)
            elif len(stack) >= 1 and op == 'C':
                stack.pop()
            elif op != '+' and op != 'D' and op != 'C':
                stack.append(int(op))
        
        return sum(stack)

#Time: O(n)
#Space: O(n)