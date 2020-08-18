"""Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward."""

"""Runtime: 48 ms, faster than 97.34% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.8 MB, less than 81.23% of Python3 online submissions for Palindrome Number."""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        try:
            return x == int(str(x)[::-1])
        except Exception:
            return False
