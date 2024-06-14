from typing import List


def minIncrementForUnique(nums: List[int]) -> int:
    nums.sort()
    many_moves = 0

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            increment = nums[i - 1] - nums[i] + 1
            nums[i] += increment
            many_moves += increment

    return many_moves


print(minIncrementForUnique([1, 2, 2]))
print("\n------\n")
print(minIncrementForUnique([3, 2, 1, 2, 1, 7]))
