class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """

        result = prices[:]

        n = len(prices)
        stack = []

        for i,val in enumerate(prices):
            
            while( len(stack) and stack[-1][0] >=  val  ):
                prevVal,index = stack.pop()
                amount = abs(prevVal - val) 
                result[index] = amount

            stack.append([val,i])

           


        return result
        