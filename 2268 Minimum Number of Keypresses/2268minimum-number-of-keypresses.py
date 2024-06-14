class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1
        
        count = sorted(count, reverse = True)

        #return sum(count[:9]) + 2 * sum(count[9: 18]) + 3 * sum(count[18:])

        res = 0
        keyPresses = 0

        for i in range(len(count)):
            if i % 9 == 0:
                keyPresses += 1
            res += keyPresses * count[i]
        
        return res

#Time: O(n + 26log26) = O(n)
#Space: O(1)