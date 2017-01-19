class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        
        i = 0
        j = 0
        
        while j < len(nums):
            while j < len(nums)  and nums[j] == 0:
                j += 1
                
            while j > i and nums[i] != 0:
                i += 1
            
            if j < len(nums) and j > i:    
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
            
            
            
            
            
            
                    
                    
                    
            
            
                
                
                
                
                