class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        tag = 0
        result = ""
        
        if num < 0:
            num = abs(num)
            tag = 1
            
        if num < 7:
            if tag == 1:
                return "-" + str(num)
            return str(num)
        
        while(num/7 > 0):
            remain = num%7
            result += str(remain)
            num = num/7
        
        result += str(num)
        result = result[::-1]
        
        if tag == 1:
            result = "-" + result
            
        return result