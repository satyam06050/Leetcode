class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = [0, 0, 0]   # for 'a', 'b', 'c'
        l = 0
        ans = 0

        for r in range(len(s)):
            freq[ord(s[r]) - ord('a')] += 1

            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                ans += len(s) - r
                freq[ord(s[l]) - ord('a')] -= 1
                l += 1

        return ans
