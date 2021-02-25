class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxWealth = 0
        for account in accounts:
            wealth = 0
            for balance in account:
                wealth += balance
            maxWealth = max(maxWealth, wealth)
            
        return maxWealth