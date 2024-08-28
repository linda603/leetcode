class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visit = set()
        res = set()

        for i in range(len(s) - 9):
            substring = s[i: i + 10]
            if substring in visit:
                res.add(substring)
            else:
                visit.add(substring)
        
        return res

#Time: O((n - 10)*10). It takes O(10) to build a substring of length 10
#Space: O((n - 10)*10)