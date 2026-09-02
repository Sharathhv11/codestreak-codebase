class Solution:
    def sortStack(self, st):
        # code here 
        def helper(st):
            if( len(st) == 0 ):
                return 
            
            num = st.pop()
            helper(st)
            
            if( len(st) == 0 ):
                st.append(num)
            else:
                helperStack = []
                while( len(st) != 0 and st[-1] > num ):
                    helperStack.append(st.pop())
                st.append(num)
                
                while( len(helperStack) != 0 ):
                    st.append(helperStack.pop())
                    
                    
        helper(st)