class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(numRows - 1):
            tempArr = [0] + result[-1] + [0]
            newRow = []
            for j in range(len(result[-1]) + 1):
                newRow.append(tempArr[j] + tempArr[j + 1])
            result.append(newRow)
        return result

#Time: O(n^2)
#Space: O(n^2)