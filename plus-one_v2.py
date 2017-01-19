class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        if not digits:
            return digits
            
        
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        for d in range(len(digits) -1, -1, -1):
            if digits[d] == 9:
                digits[d] = 0
                
            else:
                digits[d] += 1
                break
               
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits