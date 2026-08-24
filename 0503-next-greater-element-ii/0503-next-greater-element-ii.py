class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        # Traverse twice because the array is circular
        for i in range(2 * n):
            index = i % n

            while stack and nums[stack[-1]] < nums[index]:
                ans[stack.pop()] = nums[index]

            if i < n:
                stack.append(index)

        return ans