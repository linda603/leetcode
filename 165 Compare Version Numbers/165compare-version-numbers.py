class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        for i in range(max(len(v1), len(v2))):
            val1 = int(v1[i]) if i < len(v1) else 0
            val2 = int(v2[i]) if i < len(v2) else 0
            if val1 < val2:
                return -1
            elif val1 > val2:
                return 1
        return 0

# Time: O(n1 + n2 + max(n1, n2))
# Space: O(n1 + n2)  