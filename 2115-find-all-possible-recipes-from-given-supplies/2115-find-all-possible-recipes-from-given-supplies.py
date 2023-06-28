class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graphDict = defaultdict(list)
        indegreeCnt = defaultdict(int)
        for i, recipe in enumerate(recipes):
            indegreeCnt[recipe] = len(ingredients[i])
            for ing in ingredients[i]:
                graphDict[ing].append(recipe)
        
        answer = []
        bfs_queue = deque(supplies)
        recipes = set(recipes)

        while bfs_queue:
            curr = bfs_queue.popleft()
            if curr in recipes:
                answer.append(curr)
            for child in graphDict[curr]:
                indegreeCnt[child] -= 1
                if indegreeCnt[child] == 0:
                    bfs_queue.append(child)
        
        return answer
                
