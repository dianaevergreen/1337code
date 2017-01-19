class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        init = 0
        end = len(nums) - 1
        
        
        while init <= end:
            if nums[init] == val:
                if nums[end] != val:
                    nums[init], nums[end] = nums[end], nums[init]
                    init += 1
                    end -= 1
                else:
                    end -= 1
                    
            else:
                init += 1
                
        return init