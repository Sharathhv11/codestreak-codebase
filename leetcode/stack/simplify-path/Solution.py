class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """


        n = len(path)
        stack = []

        i = 0
        while( i < n ):
            char = path[i]
            if( char == '/' ):
                i+=1
                continue

            subString = ""
            while( i < n and path[i] != '/' ):
                subString += path[i]
                i+=1
                

            if( subString == ".." ):
                if( len(stack) ):
                    stack.pop()
            elif( subString != "." ):
                stack.append(subString)

        return "/"+"/".join(stack)

        