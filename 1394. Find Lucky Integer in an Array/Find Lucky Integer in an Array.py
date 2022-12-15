class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map = {}
        res = -1
        for i in arr:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        for key  in map:
            if key == map[key]:
                if key > res:
                    res = key
        return res
