class Solution:
    def numTrees(self, n: int) -> int:
        #numTree[4] = numTree[0] * numTree[3] + 
        #              numTree[1] * numTree[2] +
        #               numTree[2] * numTree[1] +
        #               numTree[3] * numTreep[0]
        numTree = [1] * (n + 1)

        # 0 node -> numTree[0] = 1
        # 1 node -> numTree[1] = 1
        for node in range(2, n + 1):
            total = 0
            for root in range(1, node + 1):
                left = root - 1
                right = node - root
                total += numTree[left] * numTree[right]
            numTree[node] = total
        return numTree[n]

#Time: O(n^2)
#Space: O(n) due to numTree