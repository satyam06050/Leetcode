class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num=""
        for i in s:
            num+=str(ord(i)-ord("a")+1)
    
        for j in range(k):
            total=0    
            for l in num:
                total+=int(l)
            num=str(total)    


        return total        

        
