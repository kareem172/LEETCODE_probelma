class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i in range(len(nums)):
            if not nums[i] in map:
                map[nums[i]] = [i]
            else:
                map[nums[i]].append(i)
        
        for key in map:
            if len(map[key]) > 1:
                for i in range(len(map[key])-1):
                    if abs(map[key][i] - map[key][i + 1]) <= k:
                        return True
                    
        return False
        