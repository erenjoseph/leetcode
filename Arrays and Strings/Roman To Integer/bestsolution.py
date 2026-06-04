class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        out = 0
        for i in range(len(s)):
            if i + 1 < len(s) and nums[s[i]] < nums[s[i + 1]]:
                out -= nums[s[i]]
            else:
                out += nums[s[i]]
        return out
