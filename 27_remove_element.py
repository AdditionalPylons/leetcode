"""Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length."""


"""Runtime: 36 ms, faster than 57.44% of Python3 online submissions for Remove Element.
Memory Usage: 13.8 MB, less than 68.23% of Python3 online submissions for Remove Element."""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        shift_vector = 0
        final_length = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                shift_vector -=1
                final_length -=1
            elif shift_vector != 0:
                nums[i+shift_vector] = nums[i]
        return final_length
