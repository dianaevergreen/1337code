class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        for x in 2,3,5:
            while num % x == 0 < num:
                num /= x
        return num == 1