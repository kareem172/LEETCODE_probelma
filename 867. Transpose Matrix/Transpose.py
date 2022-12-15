class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        new = [[0 for _ in range(m)]  for i in range(n)] 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == j:
                    new[i][j] = matrix[i][j]
                else:
                    new[j][i]= matrix[i][j]          

        return new
