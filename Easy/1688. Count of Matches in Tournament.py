def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        played = 0
        while n > 1:
            matches = n//2
            advance = n - matches
            played = played + matches
            n = advance
        return played
        
