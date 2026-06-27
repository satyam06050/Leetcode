class Solution:
    def trailingZeroes(self, n: int) -> int:
        t_z=0
        while n>=5:
            n=n//5
            t_z+=n
        return t_z    

        