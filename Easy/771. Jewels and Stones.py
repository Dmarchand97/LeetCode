def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewz_count = 0
        j_list = list(J)
        for stone in S:
            if stone in j_list:
                jewz_count = jewz_count + 1
        return jewz_count
