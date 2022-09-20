def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        output = 0
        for number in range(n):
            output ^= (start + 2 * number)
        return output
