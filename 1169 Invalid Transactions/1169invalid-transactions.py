class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []

        for i in range(len(transactions)):
            for j in range(len(transactions)):
                if i == j:
                    continue
                name1, time1, amount1, city1 = transactions[i].split(",")
                name2, time2, amount2, city2 = transactions[j].split(",")
                if int(amount1) > 1000:
                    res.append(transactions[i])
                    break
                if name1 == name2 and city1 != city2 and abs(int(time1) - int(time2)) <= 60:
                    res.append(transactions[i])
                    break
        return res

# Time: O(n^2)
# Space: O(1)