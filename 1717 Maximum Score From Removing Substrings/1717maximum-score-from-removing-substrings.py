class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def removePair(pair, score):
            nonlocal s
            total = 0
            stack = []

            for c in s:
                if stack and stack[-1] == pair[0] and c == pair[1]:
                    stack.pop()
                    total += score
                else:
                    stack.append(c)
            # Update string s after removing all pair
            s = "".join(stack)
            return total

        res = 0
        pair = "ab" if  x > y else "ba"
        res += removePair(pair, max(x, y))
        res += removePair(pair[::-1], min(x, y))
        
        return res

#Time: O(2n)
#Space: O(n)
