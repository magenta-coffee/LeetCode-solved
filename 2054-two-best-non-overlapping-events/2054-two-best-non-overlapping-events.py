class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        allE = []
        for (s,e,v) in events:
            allE.append((s, v, 1))
            allE.append((e+1,v, 0))
        
        allE.sort(key=lambda x : (x[0], x[2]))
        result = 0
        value = 0
        for (t, v, startLabel) in allE:
            if startLabel == 1:
                result = max(result, value+v)
            else:
                value = max(value, v)
        
        return result
   