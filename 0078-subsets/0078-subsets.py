class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        def s(index,ans):
            if index==len(nums):
                result.append(ans[:])

                return
            ans.append(nums[index])
            s(index+1,ans)
            ans.pop()
            s(index+1,ans)
        s(0,[])
        return result     
        