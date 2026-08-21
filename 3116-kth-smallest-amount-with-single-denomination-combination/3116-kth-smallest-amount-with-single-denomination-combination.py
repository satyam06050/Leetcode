from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def lcm(a, b):
            return a * b // gcd(a, b)

        def count(x):
            total = 0
            n = len(coins)

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):
                multiple = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        multiple = lcm(multiple, coins[i])
                        bits += 1

                        if multiple > x:
                            break

                if bits % 2 == 1:
                    total += x // multiple
                else:
                    total -= x // multiple

            return total

        left, right = 1, min(coins) * k

        # Binary Search
        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left