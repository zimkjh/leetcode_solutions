class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxSquare = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        maxVal = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    maxSquare[i][j] = int(matrix[i][j])
                    maxVal = max(maxVal, int(matrix[i][j]))
                    continue
                if matrix[i][j] == "0":
                    continue
                tempVal = min(maxSquare[i-1][j], maxSquare[i][j-1], maxSquare[i-1][j-1]) +1
                maxSquare[i][j] = tempVal
                maxVal = max(maxVal, tempVal)
        return maxVal * maxVal
        
                
        