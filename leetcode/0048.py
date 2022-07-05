class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            for j in range(i):
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
        for row in matrix:
            row.reverse()
        
        # n = len(matrix) - 1
        # nt = len(matrix) // 2 + len(matrix) % 2
        # for i in range(nt):
        #     for j in range(nt - len(matrix) % 2):
        #         tmp = matrix[i][j]
        #         matrix[i][j] = matrix[n - j][i]
        #         matrix[n - j][i] = matrix[n - i][n - j]
        #         matrix[n - i][n - j] = matrix[j][n - i]
        #         matrix[j][n - i] = tmp
