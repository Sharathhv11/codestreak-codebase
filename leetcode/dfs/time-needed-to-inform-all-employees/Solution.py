class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        
        maxTime = 0
        graph = dict()
        for index,man in enumerate(manager):
            if( man not in graph ):
                graph[man]= []

            graph[man].append(index) 
        
      

        def dfs(root,time):
            nonlocal maxTime
            if( root not in graph ):
                maxTime = max(maxTime,time)
                return
        
            for empID in graph[root]:
               dfs(empID,time+informTime[root])
  
        dfs(graph[-1][0],0)

        return maxTime