class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return self.dfs(n, 0)
    
    def dfs(self, target, i):
        if target == 0:
            return True
        if target < 3 ** i:
            return False
        include_i = self.dfs(target - 3 ** i, i + 1)
        skip_i = self.dfs(target, i + 1)
        return include_i or skip_i

# Time: O(2^x): x: height of the tree = O(2^(log3(n))) < O(n)
# Space: O(x)