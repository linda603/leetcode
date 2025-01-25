class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        visited = set()

        for c in s:
            while stack and c not in visited and ord(stack[-1]) > ord(c) and count[stack[-1]] > 1:
                remove_char = stack.pop()
                count[remove_char] -= 1
                visited.remove(remove_char)
            if c in visited:
                count[c] -= 1
            else:
                stack.append(c)
                visited.add(c)
        return "".join(stack)






"""
s = "cbacdcbc"
           i
c: 4
b: 2
a: 1
d: 1

c b a d
-> a c d b

cbad
bacd
adcb


"""