class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimum = total = 0
        for i in nums:
            total += i
            minimum = min(minimum , total)
        
        return -minimum + 1
