class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #add and sort
        nums3 = nums1 + nums2
        nums3.sort()
        
        l=len(nums3)
        
        #if len is even
        if l%2 == 0:
            return (nums3[l//2]+nums3[l//2-1])/2
        #if len is odd - middle
        return nums3[l//2]
        
#144 ms 14.2 MB