# Given a string s, find the length of the longest
# substring
#  without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


def lengthOfLongestSubstring(s: str) -> int:

    longest = 0
    start = 0
    used_char_map = {}

    for i, char in enumerate(s):

        print(f"[{i}]char: {char}")

        if char in used_char_map and used_char_map[char] >= start:

            print(f"char: {char} | start: {start} | i: {i} | {used_char_map}")

            longest = max(i - start, longest)

            # exit
            start = used_char_map[char] + 1

        used_char_map[char] = i
        longest = max(i - start + 1, longest)

    print(longest)
    return longest


# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("dvdf"))
print("\n----\n")
print(lengthOfLongestSubstring("aab"))
