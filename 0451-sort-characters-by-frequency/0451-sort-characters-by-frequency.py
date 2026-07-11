class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        arr=list(freq.items())
        arr.sort(key=lambda x:x[1],reverse=True)

        ans=""
        for ch,count in arr:
            ans+=ch*count    
        return ans    

        