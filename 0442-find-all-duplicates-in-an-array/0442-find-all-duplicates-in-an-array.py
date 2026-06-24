
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        freq={}
        ans=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i,j in freq.items():
            if j==2:
                ans.append(i)
        return ans        


        