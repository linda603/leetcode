class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()

        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            c = searchWord[i]
            print(c)
            while l <= r and (len(products[l]) <= i or  products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1
            # now range between l and r is valid
            suggestion = []
            for j in range(min(3, r - l + 1)):
                suggestion.append(products[l + j])
            res.append(suggestion)
        return res

#Time: O(nlogn + m*3 + n. n: len(products), m: len(searchWord).
#Space: O(n*m)