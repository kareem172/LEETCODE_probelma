class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        m = len(mat)
        for i in range(m):
            for j in range(m):
                if i == j:
                    res += mat[i][j]
                if i + j == m - 1:
                    res += mat[i][j]
                    
        if m % 2 == 1:
            res -= mat[m//2][m//2]
        return res