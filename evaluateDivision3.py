
class Solution:
    def addEdge(graph,from_, to, val):
        if from_ in graph:
            graph[from_].append((to, val))
        else:
            graph[from_] = [(to, val)]
            
    def createGraph(equations, values): 
        graph = {}
        
        for (from_,to), val in zip(equations,values):
            Solution.addEdge(graph, from_, to, val)
            Solution.addEdge(graph, to, from_, 1/val)
        return graph
    
    def calcEquation(equations , values, queries):
        graph = Solution.createGraph(equations, values)
    
        results = []

        def dfs(from_,to,runningVal):
            seen.add(from_)
            
            if from_ == to:
                return runningVal

            for neighbour,val in graph[from_]:
                if  neighbour not in seen:
                    ans = dfs(neighbour,to,runningVal * val)
                    if ans != -1:
                        return ans
            return None

        for from_,to in queries:
                if  (from_ not in graph) or  (to not in graph):
                    ans = -1
                elif from_ == to:
                    ans = 1
                else:
                    seen = set()                
                    ans = dfs(from_,to,1)

                results.append(ans)
        return results
                
print(Solution.calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
    
                    
        
        
        