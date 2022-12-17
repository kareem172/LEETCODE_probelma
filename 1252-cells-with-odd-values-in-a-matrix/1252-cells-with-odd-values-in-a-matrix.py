class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        odds = 0
        rows = [0] * m
        col = [0] * n
        
        
        for i, j in indices:
            rows[i] += 1
            col[j] +=1
        
        for i in range(m):
            for j in range(n):
                if (rows[i] + col[j]) % 2 == 1:
                    odds += 1
                    
        return odds
        