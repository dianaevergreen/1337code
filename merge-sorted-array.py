class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
    
        """
        
        cm = m
        cn = n-1
        cmn = m+n-1
        
        while cm > 0 and cn >= 0:
            
            if nums1[cm-1] > nums2[cn]:
                nums1[cmn] = nums1[cm-1]
                cmn -= 1
                cm -= 1
            else:
                nums1[cmn] = nums2[cn]
                cn -= 1
                cmn -= 1
                
        if cm == 0 and n > 0:
            nums1[:cn+1] = nums2[:cn+1]
            