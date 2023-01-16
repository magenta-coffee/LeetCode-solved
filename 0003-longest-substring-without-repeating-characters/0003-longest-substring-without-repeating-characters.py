class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1: 
            return len(s)

        maxNum, resultNum = 0, 0
        resultString = ''
        
        for i in s:
            if i in resultString:
                resultString = resultString[resultString.index(i)+1:] + i
                resultNum = len(resultString)
            else:
                resultString += i
                resultNum += 1
            if resultNum >= maxNum:
                 maxNum = resultNum
                    
        return maxNum
            
        
            