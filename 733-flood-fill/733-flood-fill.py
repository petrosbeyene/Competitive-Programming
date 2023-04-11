class Solution:
    def isValid(self, sr, sc, row, col):
        if sr < 0 or sr >= row:
            return False
        elif sc < 0 or sc >= col:
            return False
        else:
            return True

    def dfs(self, image, sr, sc, color, row, col, targetColor):
        if not self.isValid(sr, sc, row, col):
            return 
        if image[sr][sc] == color or image[sr][sc] != targetColor:
            return
        
        image[sr][sc] = color
        self.dfs(image, sr+1, sc, color, row, col, targetColor)
        self.dfs(image, sr-1, sc, color, row, col, targetColor)
        self.dfs(image, sr, sc+1, color, row, col, targetColor)
        self.dfs(image, sr, sc-1, color, row, col, targetColor)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        targetColor = image[sr][sc]
        self.dfs(image, sr, sc, color, row, col, targetColor)

        return image
