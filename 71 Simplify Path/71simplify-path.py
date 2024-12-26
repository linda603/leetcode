class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = ""
        res = []
        path += "/" # to add the last word to res

        for c in path:
            if c == "/":
                if curr:
                    if curr == "..":
                        if res:
                            res.pop()
                    elif curr != ".":
                        res.append(curr)
                curr = ""
            else:
                curr += c
        print(res)
        return "/" + "/".join(res)

# Time: O(n)
# Space: O(n)