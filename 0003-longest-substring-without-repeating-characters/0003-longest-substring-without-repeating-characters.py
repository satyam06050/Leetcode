class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash1=[-1]*256
        l,r,max_len=0,0,0
        n=len(s)
        while r<n:
            if hash1[ord(s[r])] != -1:
                if hash1[ord(s[r])]>=l:
                
                    l=hash1[ord(s[r])]+1
            max_len=max(max_len,r-l+1)
            hash1[ord(s[r])]=r

            r+=1
        return max_len        



        