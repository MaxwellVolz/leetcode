# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:

    shortest = min([len(x) for x in strs])
    longest = 0

    for x in range(0, shortest):

        if len(set([z[x] for z in strs])) == 1:
            longest += 1
        else:
            return strs[0][:longest]

    if longest == 0:
        return ""

    return strs[0][:longest]


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
