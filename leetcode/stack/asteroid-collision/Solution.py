class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []
        
        for a in asteroids:
            
            if( not len(stack) or a > 0 or stack[-1] < 0 ):
                stack.append(a)
            else:
                destroyed = False
                while( len(stack)  ):
                    a1 = stack[-1] # always be the positive 
                    a2 = abs(a) #always negative

                    if( a1 < 0 ):
                        break

                    if( a1 == a2 ):
                        stack.pop()
                        destroyed = True
                        break
                    elif( a1 < a2 ):
                        stack.pop()
                    else:
                        destroyed = True
                        break
                if( not destroyed ):
                    stack.append(a)
        return (stack)

                    
            
        