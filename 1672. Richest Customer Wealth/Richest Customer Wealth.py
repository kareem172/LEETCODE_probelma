class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for arr in accounts:
            if sum(arr) > max:
                max = sum(arr)

        return max
