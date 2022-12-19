class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minimum = len(list2)+ len(list1)
        res = []
        map = {}
        for i in range(len(list1)):
            map[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in map:
                if (j + map[list2[j]]) == minimum :
                    res.append(list2[j])
                elif j + map[list2[j]] < minimum :
                    minimum = j + map[list2[j]] 
                    res = [list2[j]]
        return res