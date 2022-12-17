class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        map = {'type':0, 'color':1 , 'name':2}
        res = 0
        for item in items:
            if ruleValue == item[map[ruleKey]]:
                res += 1 
                
        return res
        
        