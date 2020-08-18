"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

"""Runtime: 24 ms, faster than 97.45% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.8 MB, less than 71.50% of Python3 online submissions for Reverse Integer."""


class Solution:
    def reverse(self, x: int) -> int:
        num_string = str(x)
        if num_string[0] == "-":
            answer = int("-"+num_string[:0:-1])
        else:
            answer = int(num_string[::-1])
        if  answer < -2**31 or answer > (2**31)-1:
            return 0
        else:
            return answer
