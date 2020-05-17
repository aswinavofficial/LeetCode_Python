# Given a string s, find the longest palindromic substring in s
# --- Example
# longestPalindrome("cbbd") --> "bb"
# longestPalindrome("abba") --> "abba"
# longestPalindrome("a") --> "a"


class Solution:
    def retrieve_pal(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return s[left + 1 : right]

    def longestPalindrome(self, s):
        res = ""

        for i in range(len(s)):
            current = self.retrieve_pal(s, i - 1, i + 1)
            in_between = self.retrieve_pal(s, i, i + 1)
            res = max(current, in_between, res, key=len)
        return res
