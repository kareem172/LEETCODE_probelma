class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min = max(arr)
        arr.sort()
        res = []
        for i in range(1,len(arr)):
            if arr[i] - arr[i - 1] < min :
                min = arr[i] - arr[i - 1] 
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min :
                temp = [arr[i - 1], arr[i] ]
                res.append(temp)
        return res