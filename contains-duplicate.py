class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        settie = set(nums)
        
        if len(settie) != len(nums):
            return True
        else:
            return False