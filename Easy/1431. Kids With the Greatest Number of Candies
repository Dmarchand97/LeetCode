def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        fin_candies = []
        top_candy = max(candies)

        for kid in candies:
            new_kid = kid + extraCandies
            if new_kid >= top_candy:
                fin_candies.append(True)
            else:
                fin_candies.append(False)
        return(fin_candies)
