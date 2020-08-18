"""Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned."""



"""Runtime: 32 ms, faster than 85.51% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.6 MB, less than 95.06% of Python3 online submissions for String to Integer (atoi)."""





import re

class Solution:
    def myAtoi(self, str):
        pattern = re.compile("(^\s*[-+]?[0-9]+)")
        match = pattern.search(str)
        max = (2**31)-1
        min = -2**31
        if match is not None:
            if int(match.group(1)) > max:
                return max
            elif int(match.group(1)) < min:
                return min
            return int(match.group(1))
        return 0
