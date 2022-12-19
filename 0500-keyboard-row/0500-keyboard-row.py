class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        
        for word in words:
            value = set(word.lower())
            if value <= set(row1) or value <= set(row2) or value <= set(row3):
                res.append(word)
        return res
        