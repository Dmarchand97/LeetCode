class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        maxlist = []
        for i in accounts:
            maxlist.append(sum(i))
        return max(maxlist)
        
