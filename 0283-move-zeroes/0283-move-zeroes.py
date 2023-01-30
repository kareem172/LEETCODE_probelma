class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = len(nums) - 1
        index = 0
        while index <= last:
            if nums[index] == 0:
                for i in range(index, last):
                    nums[i] = nums[i + 1]
                nums[last] = 0
                last = last - 1
            else: index += 1
