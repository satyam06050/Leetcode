from fractions import gcd

class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Count how many even and odd numbers exist up to n
        even_count = n // 2
        odd_count = (n + 1) // 2
        
        # Calculate sums instantly using O(1) formulas
        sumEven = even_count * (even_count + 1)
        sumOdd = odd_count * odd_count
        
        return n
