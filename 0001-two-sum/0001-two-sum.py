class Solution:
    def twoSum(self, nums, target):
        i,j=0,0
        sum=0
        for i in range(len(nums)-1):
            
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if sum==target:
                    return [i,j]
                else:
                    j+=1
            i+=1            



       