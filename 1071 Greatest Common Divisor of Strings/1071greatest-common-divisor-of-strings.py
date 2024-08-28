class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isCommonDivisor(i):
            if len1 % i != 0 or len2 % i != 0:
                return False
            if str1 == str1[:i] * (len1 // i) and str2 == str1[:i] * (len2 // i):
                return True
            return False

        for i in range(min(len1, len2), 0, -1):
            if isCommonDivisor(i):
                return str1[:i]
        
        return ""

#Time: O(min(m,n)*(m+n))
#Space: O(m+n)