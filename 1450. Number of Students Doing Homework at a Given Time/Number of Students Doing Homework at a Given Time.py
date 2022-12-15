class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        student = 0
        for a, b in zip(startTime, endTime):
            if (a<= queryTime <= b):
                student += 1
        
        return student
