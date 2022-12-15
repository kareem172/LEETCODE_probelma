class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum = 0
        length = len(arr)
        sums = [0] * (length+1)
        for i in range(len(arr)):           
            sums[i + 1] = sums[i]+ arr[i]
        
        for i in range(length):
            for j in range(0, length, 2):
                if i + j < length:
                    sum += sums[i + j + 1] - sums[i]

        return sum
