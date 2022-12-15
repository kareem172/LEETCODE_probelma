class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        while(k > 0):
            temp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n-1):
                   temp[i][j+1] = grid[i][j]

            for i in range(m-1):
                temp[i+1][0] = grid[i][n-1]

            temp[0][0] = grid[m - 1][n - 1]
            k -= 1
            grid = temp
        return grid
