class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Map Roman numeral characters to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        n = len(s)
        
        # 2. Iterate through the string by indices
        for i in range(n):
            # If the current value is less than the next value, subtract it
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
                ans -= roman_map[s[i]]
            # Otherwise, add it to the total
            else:
                ans += roman_map[s[i]]
                
        return ans
