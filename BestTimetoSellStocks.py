--Best time to buy and sell stocks LC

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        min = 100000
        for i in prices:
            if (i < min):
                min = i
            elif (i - min > max):
                max = i - min
                    
                    
        return max
