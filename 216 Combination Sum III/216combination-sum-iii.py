class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(i, curr, total):
            print("curr:", curr)
            if len(curr) == k:
                if total == n:
                    res.append(curr.copy())
                return
            for j in range(i, 10):
                curr.append(j)
                backtrack(j + 1, curr, total + j)
                curr.pop()
            
        backtrack(1, [], 0)
        return res

#Time: O((9!/(9-k)!)*k) 9 choices -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 choice
#Space: O(k)