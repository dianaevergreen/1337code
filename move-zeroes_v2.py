class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        i, j = 0, 0
        
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
            
        rest = len(nums) - i
        
        for x in range(len(nums)-1, i-1, -1):
            nums[x] = 0
                    
                    
                    
            
            
                
                
                
                
                