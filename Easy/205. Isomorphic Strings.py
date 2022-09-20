# 205. Isomorphic Strings



def isIsomorphic(s: str, t: str) -> bool:
    """This is the solution from LeetCode"""
    
    mapping_s_t = {}
    mapping_t_s = {}
    
    for c1, c2 in zip(s, t):
        
        # Case 1: No mapping exists in either of the dictionaries
        if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1
        
        # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
        # it doesn't match in either of the dictionaries or both            
        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False
        
    return True


def isIsomorphic2(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    compare each letter in each list. Wherever one letter is in first list
    another letter should be in the same locations in the second.
    if not return false.

    This is how I did it.
    Runtime: 50 ms, faster than 59.24% of Python online submissions for Isomorphic Strings.
    Memory Usage: 17.1 MB, less than 6.89% of Python online submissions for Isomorphic Strings.
    """
    sindex = []
    tindex = []
    # check if lists are same len
    if len(s) != len(t):
        return False
    for i, x in zip(s, t):
        sindex.append(s.index(i))
        tindex.append(t.index(x))

    if sindex == tindex:
        return True
    else:
        return False


a = 'paper'
b = 'title'
print(isIsomorphic(a, b))
