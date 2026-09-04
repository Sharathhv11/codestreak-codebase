class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """

        if( not len(self.stack) or self.stack[-1][0] > price ):
            self.stack.append([price,1])
            return 1

        total = 1
        while( len(self.stack) and self.stack[-1][0] <= price ):
            prevPrice,spanCount = self.stack.pop()
            total += spanCount

        self.stack.append([price,total])

        return total

        

        

        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)