class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3=nums1+nums2
        num3.sort()
        n=len(num3)
        median=0
        if n %2 ==0:
            n1=n//2
            
            median=(num3[n1]+num3[n1-1])/2
        else:
            median=num3[n//2]    

        return median    

        