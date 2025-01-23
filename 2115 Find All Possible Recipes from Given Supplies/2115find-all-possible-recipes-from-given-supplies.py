class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        num_ingreds = {} # recipe: number of ingredients
        required = defaultdict(list) # ingredient: map with list of recipes

        for recipe, required_ingre in zip(recipes, ingredients):
            num_ingreds[recipe] = len(required_ingre)
            for ingre in required_ingre:
                required[ingre].append(recipe)
        
        queue = deque(supplies)
        res = []

        while queue:
            ingre = queue.popleft()
            for recipe in required[ingre]:
                num_ingreds[recipe] -= 1
                if num_ingreds[recipe] == 0:
                    res.append(recipe)
                    queue.append(recipe)
        return res

# Time: O(E + V) = O(len(ingredients) + len(supplies))
# Space: O(V + E + V) = O(E + V)