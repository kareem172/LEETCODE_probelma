class Solution:
    def longestPalindrome(self, s: str) -> int:
        map = {}
        res = 0
        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1
        for key in map:
            if map[key] % 2 == 0:
                res += map[key]
            else :
                res += map[key] - 1
        
        if res < len(s) and res % 2 ==0:
            res += 1
            
        return res
            