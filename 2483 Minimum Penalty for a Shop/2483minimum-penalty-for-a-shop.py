class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefixN = [0] * (n + 1)
        postfixY = [0] * (n + 1)
        result = 0
        minPenalty = float("inf")

        for i in range(1, n + 1):
            prefixN[i] = prefixN[i - 1]
            if customers[i - 1] == 'N':
                prefixN[i] += 1
        
        for i in range(n - 1, -1, -1):
            postfixY[i] = postfixY[i + 1]
            if customers[i] == 'Y':
                postfixY[i] += 1
        
        for i in range(n + 1):
            currPenalty = prefixN[i] + postfixY[i]
            if currPenalty < minPenalty:
                minPenalty = currPenalty
                result = i
        
        return result

#Time: O(3n) = O(n)
#Space: O(2(n + 1)) = O(n)
