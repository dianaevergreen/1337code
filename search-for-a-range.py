class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        s = set()
        for i in nums:
            s.add(i)
            
        if target not in s:
            return [-1, -1]
        
        
        mid = (len(nums))/2
        
        while mid >= 0 and mid < len(nums):
            
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                
                mid = mid - 1
            else:
                mid = (mid + 1 + len(nums)) / 2
                
        
                
        if mid > len(nums)-1 or mid < 0:
            return [-1, -1]
        
        
        
        init, fin = mid, mid
        
        
        if init != 0:
            start_init = 0
            end_init = mid - 1
            mid_init = (end_init) / 2
        
        
            while start_init <= end_init:
                if nums[mid_init] == target:
                    init = mid_init
                    end_init = mid_init - 1
                    mid_init = (end_init ) / 2
                else:
                    start_init = mid_init + 1
                    mid_init = (start_init + end_init) / 2
                
                
            
        
        if fin != len(nums) -1 :
            
            start_fin = mid + 1
            end_fin = len(nums) - 1
            mid_fin= (start_fin + end_fin)/2
        
            while start_fin <= end_fin:
                if nums[mid_fin] == target:
                    fin = mid_fin
                
                    start_fin = mid_fin + 1
                    mid_fin = (start_fin + end_fin) / 2
                
                else:
                    end_fin = mid_fin - 1
                    mid_fin = (start_fin + end_fin) / 2
                
            
        return [init, fin]
            
        
        
        
        
        