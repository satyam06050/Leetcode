class Solution:
    def relativeSortArray(self, arr1, arr2):

        freq = {}

        # build frequency map
        for num in arr1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ans = []

        # place arr2 elements first
        for num in arr2:
            while freq[num] > 0:
                ans.append(num)
                freq[num] -= 1

            del freq[num]

        # remaining elements
        remain = []

        for key in freq:
            while freq[key] > 0:
                remain.append(key)
                freq[key] -= 1

        remain.sort()

        return ans + remain