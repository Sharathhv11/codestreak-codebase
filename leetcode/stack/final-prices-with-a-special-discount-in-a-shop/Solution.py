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
            if( i == 0 ):
                stack.append([val,i])
                continue

            
            buff = []
            while( len(stack) and stack[-1][0] < val ):
                buff.append(stack.pop())

            
      
            while( len(stack) and stack[-1][0] >=  val  ):
                prevVal,index = stack.pop()
                amount = abs(prevVal - val) 
                result[index] = amount

            stack.append([val,i])

            while( len(buff) ):
                stack.append(buff.pop())



        return result
        