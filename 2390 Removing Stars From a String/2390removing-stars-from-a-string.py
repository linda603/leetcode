class Solution:
    def removeStars(self, s: str) -> str:
        res = []

        for char in s:
            if char == "*":
                res.pop()
            else:
                res.append(char)
        
        return "".join(res)

#Time: O(n)
#Space: O(n)

