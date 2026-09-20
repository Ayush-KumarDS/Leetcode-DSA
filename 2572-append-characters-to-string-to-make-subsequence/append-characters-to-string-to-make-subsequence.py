class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i = 0  # pointer for s
        j = 0  # pointer for t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1   # always move forward in s

        return len(t) - j

