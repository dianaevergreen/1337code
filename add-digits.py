class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while num >= 10:
            addition = 0
            tmp = str(num)
            
            for t in tmp:
                addition += int(t)
                
            num = addition
            
        return num
                