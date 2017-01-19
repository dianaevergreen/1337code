class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        dicti = {}
        string = [x for x in str.split()]
        if len(pattern) != len(string):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dicti.keys():
                if string[i] in dicti.values():
				    return False
                dicti[pattern[i]] = string[i]
            else:
                if dicti[pattern[i]] != string[i]:
                    return False
                    
        return True
        