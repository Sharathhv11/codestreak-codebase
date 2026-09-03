class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        result = [ 0 ] * n

        stack = []

        for i in range(n):
            temp = temperatures[i]

            while( stack and temp > stack[-1][0] ):
                pTemp,index = stack.pop()
                result[index] = i - index
            stack.append([temp,i])

        return result

         