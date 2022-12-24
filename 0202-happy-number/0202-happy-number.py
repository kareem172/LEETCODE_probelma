class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        
        while n not in visited:   
            visited.add(n)
            nums = str(n)
            if n == 1:
                return True
            sum = 0
            for num in nums:
                sum += (int(num) * int(num))
        
            n = sum
            
        