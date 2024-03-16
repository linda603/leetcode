class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        currAltitude = 0
        maxAltitude = 0

        for g in gain:
            currAltitude += g
            maxAltitude = max(maxAltitude, currAltitude)
        return maxAltitude
#Time: O(n)
#Space: O(1)
        