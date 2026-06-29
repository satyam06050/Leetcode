class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=0
        for i in digits:
            ans=ans*10+i
        ans=ans+1
        final=[]
        for i in str(ans):
            final.append(int(i))
        return final        
        