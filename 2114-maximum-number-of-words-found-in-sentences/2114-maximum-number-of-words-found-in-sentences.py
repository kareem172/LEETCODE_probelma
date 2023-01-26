class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for sentence in sentences:
            val = sentence.count(" ") + 1  
            if val > max:
                max = val
        return max
        