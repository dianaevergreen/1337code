class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
            
        flag = True
        current = nums[0]
        pos = 1
        
        while flag:
            if pos > len(nums)-1:
                flag = False
                break
            
            if nums[pos] == current:
                del nums[pos]
                
            else:
                current = nums[pos]
                pos += 1
        return len(nums)            
        
        
        