class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        sum = 0
        for num in nums:
            sum += num
            if sum >= maximum:
                maximum = sum
            if sum < 0:
                sum = 0
        return maximum