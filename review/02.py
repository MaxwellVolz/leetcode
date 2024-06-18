# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


from typing import List, Optional

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:


def addTwoNumbers(l1, l2):  # type: ignore

    l1, l2 = [str(x) for x in l1[::-1]], [str(x) for x in l2[::-1]]

    print(l1, l2)

    l1, l2 = int("".join(l1)), int("".join(l2))

    return l1 + l2


print(addTwoNumbers([2, 4, 3], [5, 6, 4]))
print(addTwoNumbers([0], [0]))
