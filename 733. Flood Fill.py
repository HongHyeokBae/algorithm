

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        type image: : List[List[int]]
        type sr: int
        type sc: int
        type newColor: int
        rtype: : List[List[int]]
        """
        rowLen, colLen = len(image), len(image[0])
        pixelStack = [(sr, sc)]
        color = image[sr][sc]

        while pixelStack:
            row, col = pixelStack.pop()
            image[row][col] = newColor;

            for d in [-1, 1]:
                if self.inBound(row+d, col, rowLen, colLen) and image[row+d][col] != newColor:
                    if image[row+d][col] == color:
                        image[row+d][col] = newColor
                        pixelStack.append((row+d, col))
                    
                if self.inBound(row, col+d, rowLen, colLen) and image[row][col+d] != newColor:
                    if image[row][col+d] == color:
                        image[row][col+d] = newColor
                        pixelStack.append((row, col+d))
                    
        return image
                             
    def inBound(self, row, col, rowLen, colLen):
        if row < 0 or row >= rowLen:
            return False
        if col < 0 or col >= colLen:
            return False
        return True