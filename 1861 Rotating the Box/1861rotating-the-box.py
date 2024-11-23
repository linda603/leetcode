class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        res = [["." for r in range(m)] for c in range(n)]

        for r in range(m):
            i = n - 1
            for c in reversed(range(n)):
                if box[r][c] == "#":
                    res[i][m - r - 1] = "#"
                    i -= 1
                elif box[r][c] == "*":
                    res[c][m - r - 1] = "*"
                    i = c - 1

        return res