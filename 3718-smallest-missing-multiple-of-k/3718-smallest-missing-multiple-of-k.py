class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiples = set(range(k, max(nums) + k + 1, k))

        for num in nums:
            multiples.discard(num)

        return min(multiples)