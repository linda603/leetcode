class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        visited = set([0])
        maxNum = 1 << n

        def dfs(n):
            if len(res) == maxNum:
                return True
            curr = res[-1]
            for i in range(n):
                nextNum = curr ^ (1 << i)
                if nextNum not in visited:
                    res.append(nextNum)
                    visited.add(nextNum)
                    if dfs(n):
                        return True
                    visited.remove(nextNum)
                    res.pop()
            return False
        dfs(n)
        return res

