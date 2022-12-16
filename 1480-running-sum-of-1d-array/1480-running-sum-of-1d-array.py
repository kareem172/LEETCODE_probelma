class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        map = {}
        res = []
        for key in range(len(nums)):
            if key - 1 in map:
                map[key] = nums[key] + map[key - 1]
                res.append(map[key])
            else:
                map[key] = nums[key]
                res.append(map[key])
        return res