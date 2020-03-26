"""
    26. Remove Duplicates from Sorted Array

    https://leetcode.com/problems/remove-duplicates-from-sorted-array/

    Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    Example 1:

    Given nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

    It doesn't matter what you leave beyond the returned length.
    Example 2:

    Given nums = [0,0,1,1,1,2,2,3,3,4],

    Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

    It doesn't matter what values are set beyond the returned length.
    Clarification:

    Confused why the returned value is an integer but your answer is an array?

    Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

    Internally you can think of this:

    // nums is passed in by reference. (i.e., without making a copy)
    int len = removeDuplicates(nums);

    // any modification to nums in your function would be known by the caller.
    // using the length returned by your function, it prints the first len elements.
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }
"""

"""
    Remember that arguments are passed by assignment in Python. 
    Since assignment just creates references to objects, 
    there’s no alias between an argument name in the caller and callee, 
    and so no call-by-reference per se.
"""


def remove_duplicates(nums):
    """
    Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

    :param nums: List[int], a sorted array nums
    :return: the new length of elements which each of appear only once
    """
    if len(nums) == 0:
        return len(nums)

    length = 1
    for i, num in enumerate(nums):
        if i == 0:
            continue
        if num != nums[length-1]:
            nums[length] = num
            length += 1

    return length


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length = remove_duplicates(nums)
    for i in range(length):
        print(nums[i])
