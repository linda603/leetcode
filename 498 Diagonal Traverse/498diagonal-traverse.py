class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        going_up = True
        r, c = 0, 0

        def out_of_bound(r, c):
            return not (r in range(m) and c in range(n))

        while not out_of_bound(r, c):
            res.append(mat[r][c])
            if going_up:
                if not out_of_bound(r - 1, c + 1):
                    r -= 1
                    c += 1
                else:
                    # check if can use a right cell then down cell
                    going_up = False
                    if not out_of_bound(r, c + 1):
                        c += 1
                    else:
                        r += 1
            else:
                if not out_of_bound(r + 1, c - 1):
                    r += 1
                    c -= 1
                else:
                    # check if can use a down cell then right cell
                    going_up = True
                    if not out_of_bound(r + 1, c):
                        r += 1
                    else:
                        c += 1
        return res

# Time: O(mn)
# Space: O(mn)