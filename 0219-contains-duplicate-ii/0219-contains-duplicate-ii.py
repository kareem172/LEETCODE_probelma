class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i in range(len(nums)):
            if not nums[i] in map:
                map[nums[i]] = i
            else:
                if abs(map[nums[i]] - i) <= k:
                    return True
                else:
                    map[nums[i]] = i
        
        return False
        