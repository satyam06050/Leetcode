class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        value=dict(sorted(freq.items(),key=lambda x:x[1],reverse=True)) 
        return list(value.keys())[0]

        