class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        r = 1 << ((x.bit_length() + 1) // 2)

        while r*r > x:
            r = (r + x // r) // 2
        
        return r