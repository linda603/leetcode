class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        res = []

        def dfs(i, curr):
            if i >= len(num):
                print("curr:", curr)
                return len(curr) >= 3
            
            for j in range(i, len(num)):
                print("Before if i, j + 1, num[i:j + 1], curr:", i, j + 1, num[i:j + 1], curr)
                if self.isValid(num[i:j + 1], curr):
                    curr.append(int(num[i:j + 1]))
                    print("j + 1, curr:", j + 1, curr)
                    if dfs(j + 1, curr):
                        return True
                    curr.pop()
            return False
        
        return dfs(0, [])
    
    def isValid(self, string, currPath):
        if len(string) > 1 and string[0] == '0': #leading 0 case, ie 09
            return False
        if len(currPath) < 2 or (currPath[-1] + currPath[-2] == int(string)):
            return True
        return False
