class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Place each number in its correct index (value x → index x-1)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # Step 2: Find first index where value is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: If all correct
        return n + 1
