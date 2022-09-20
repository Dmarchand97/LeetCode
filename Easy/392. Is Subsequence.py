def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool

    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
    of the characters without disturbing the relative positions of the remaining characters.
    (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

    Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

    My Results:
    Success
    Runtime: 19 ms, faster than 88.68% of Python online submissions for Is Subsequence.
    Memory Usage: 13.7 MB, less than 30.74% of Python online submissions for Is Subsequence.

    need premium to see solution lel
    """
    # s -> smaller list
    # s should be in t

    s_pointer = 0

    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True

    for t_pointer in range(len(t)):
        if s[s_pointer] == t[t_pointer]:
            s_pointer = s_pointer + 1
        if t_pointer == len(t)-1 or len(s) == s_pointer:
            if s_pointer == len(s):
                return True
            else:
                return False


s = "abc"
t = "ahbgdc"
a = "b"
b = "abc"

print(isSubsequence(a, b))
