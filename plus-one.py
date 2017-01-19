class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        if len(digits) == 0:
            return []
            
        
        number = int(''.join(str(x) for x in digits))
        number += 1
        
        digits = [int(x) for x in str(number)]
        
        return digits