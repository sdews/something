def two_sum(nums, target):
    """
       https://leetcode.com/problems/two-sum/ 

       Given an array of integers, return indices of the two numbers such that they add up to a specific target.

       You may assume that each input would have exactly one solution, and you may not use the same element twice.

       Example:

       Given nums = [2, 7, 11, 15], target = 9,

       Because nums[0] + nums[1] = 2 + 7 = 9,
       return [0, 1].
    """
    
    d = dict()
    for i, num in enumerate(nums):
        if num in d and d[num] != i:
            return [d[num], i]
        second_target = target - num
        d[second_target] = i


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 22))